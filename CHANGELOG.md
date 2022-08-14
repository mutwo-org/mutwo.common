# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]


## [0.9.0] - 2022-08-14

### Added
- explicit exception classes in `mutwo.common_utilities`

### Changed
- raised exceptions to custom exception classes
- package name from `mutwo.ext-common-generators` to `mutwo.common`


## [0.8.0] - 2022-03-19

### Added
- `Backtracking` and `IndexBasedBacktracking`


## [0.7.0] - 2022-02-27

### Added
- property `terminal_tuple` and `non_terminal_tuple` to `ContextFreeGrammar`


## [0.6.0] - 2022-02-27

### Added
- property `context_free_grammar_rule_tuple` to `ContextFreeGrammar`


## [0.5.0] - 2022-02-26

### Added
- chomksy submodule with support for context-free grammar

### Changed
- from `expenvelope.Envelope` to `mutwo.core_events.Envelope`

### Removed
- `expenvelope` dependency


## [0.4.0] - 2022-01-29

### Changed
- Apply refactor from first plugin to namespace package plugin structure


## [0.2.0] - 2022-01-12

### Changed
- applied movement from music related parameter and converter modules (which have been moved from [mutwo core](https://github.com/mutwo-org/mutwo) in version 0.49.0 to [mutwo.ext-music](https://github.com/mutwo-org/mutwo.ext-music))
