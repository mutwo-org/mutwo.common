import unittest

from mutwo import common_generators


class ContextFreeGrammarTest(unittest.TestCase):
    def setUp(cls):
        class StrTerminal(str, common_generators.Terminal):
            pass

        class StrNonTerminal(str, common_generators.NonTerminal):
            pass

        cls.noun = StrNonTerminal("noun")
        cls.verb = StrNonTerminal("verb")
        cls.sentence = StrNonTerminal("sentence")
        cls.cat = StrTerminal("Cat")
        cls.dog = StrTerminal("Dog")
        cls.eats = StrTerminal("eats")

        cls.context_free_grammar_rule_tuple = (
            common_generators.ContextFreeGrammarRule(cls.noun, (cls.cat,)),
            common_generators.ContextFreeGrammarRule(cls.noun, (cls.dog,)),
            common_generators.ContextFreeGrammarRule(cls.verb, (cls.eats,)),
            common_generators.ContextFreeGrammarRule(
                cls.sentence, (cls.noun, cls.verb, cls.noun)
            ),
        )

        cls.context_free_grammar = common_generators.ContextFreeGrammar(
            cls.context_free_grammar_rule_tuple
        )

    def test_get_context_free_grammar_rule_tuple(self):
        self.assertEqual(
            self.context_free_grammar.get_context_free_grammar_rule_tuple(self.noun),
            (
                self.context_free_grammar_rule_tuple[0],
                self.context_free_grammar_rule_tuple[1],
            ),
        )
        self.assertEqual(
            self.context_free_grammar.get_context_free_grammar_rule_tuple(
                self.sentence
            ),
            (self.context_free_grammar_rule_tuple[3],),
        )

    def test_resolve(self):
        resolution = self.context_free_grammar.resolve(self.sentence)
        real_leaf_set = set(" ".join(leaf.data) for leaf in resolution.leaves())
        expected_leaf_set = set(
            ["Cat eats Dog", "Dog eats Cat", "Cat eats Cat", "Dog eats Dog"]
        )
        self.assertEqual(real_leaf_set, expected_leaf_set)

    def test_resolve_with_limit(self):
        resolution = self.context_free_grammar.resolve(self.sentence, limit=1)
        real_leaf_set = set(" ".join(leaf.data) for leaf in resolution.leaves())
        expected_leaf_set = set(["noun verb noun"])
        self.assertEqual(real_leaf_set, expected_leaf_set)


if __name__ == "__main__":
    unittest.main()
