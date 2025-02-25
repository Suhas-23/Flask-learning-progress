# Branching Strategy for INSURANCE EXTRACTION repo

## Overview

This project follows a structured branching model to ensure smooth devment, testing, and deployment.

## Branch Types

### 1. `main` (Production)

-   Contains stable, production-ready code.
-   Only updated via tested pull requests from `dev` or hotfix branches.

### 2. `dev` (Active devment)

-   Base branch for all new features and bug fixes.
-   Regularly updated with merged feature and bugfix branches.

### 3. Feature Branches (`feature/<feature-name>`)

-   Used for developing new features.
-   Created from `dev` and merged back upon completion.
-   Naming Example: `feature/document-classification`

### 4. Bugfix Branches (`bugfix/<bug-name>`)

-   Used for fixing bugs before a release.
-   Created from `dev` and merged back once resolved.
-   Naming Example: `bugfix/fix-header-parsing`

### 5. Hotfix Branches (`hotfix/<issue-name>`)

-   Used for urgent fixes in production.
-   Created from `main` and merged into both `main` and `dev`.
-   Naming Example: `hotfix/urgent-extraction-fix`

### 6. Release Branches (`release/<version-number>`)

-   Created before a major release for final testing.
-   Merged into both `main` and `dev` when stable.
-   Naming Example: `release/v1.2.0`

## Workflow Summary

1. Create a feature branch for new developments.
2. Merge completed features into `dev`.
3. Before release, create a `release/<version>` branch for final testing.
4. Merge the release branch into `main` when stable.
5. Use `hotfix/<issue>` branches for urgent fixes, merging them into both `main` and `dev`.
