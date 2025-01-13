# ChestGame ♟️

<a name="readme-top"></a>

<p align="center">
  <img src="/Media/giphy.gif" alt="Chess battle">
</p>


## Project Overview

This project is a Python implementation of the classic game of chess. The goal is to create a fully functional chess game with a modular and maintainable architecture, adhering to Python’s best practices and ensuring code quality through error handling, testing, and documentation.

## Technologies and tools used

For this project we worked on these technologies
 

* [![Git][Git]][Git-url]

* [![Python][Python]][Python-url]

  <p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

## Architecture and model

The project uses the MVVM (Model-View-ViewModel) pattern to ensure a clear separation of responsibilities.

***Model*** : Contains data classes and manages business logic.

***View*** : Represents the user interface (XAML).

***ViewModel*** : Links the model to the view.

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

## Database model

The provided model must be respected without modification. Example tables:

***Users*** : Manages users.

***Monsters*** : Manages monsters.

***Spells*** : Manages spells.

***CombatLogs*** : Stores combat logs (optional).

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

## Project initialization


> [!IMPORTANT]
> To get started with this project, you'll need :

- [SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) installed on your local machine.

- [Visual Studio](https://visualstudio.microsoft.com/fr/) with WPF and Entity Framework extensions enabled.

- [Git](https://git-scm.com/downloads) for version control and collaboration.

  <p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

## Installation

> [!NOTE]
> Request access to be added as a collaborator

Clone the repository from GitHub:

```bash
     git clone https://github.com/Tokennn/Pokemon.WPF.git
     cd pokemon-like/
````

➡️ Open the project in Visual Studio.

➡️ Configure the database connection URL in the "Settings" tab.

➡️ Initialize the data by following the instructions below.

## Initialize the data

**Thanks to a preconfigured table we can import it into a new database** :

```bash

CREATE TABLE Users (
Id INT PRIMARY KEY IDENTITY,
Username NVARCHAR(50),
PasswordHash NVARCHAR(256)
);
INSERT INTO Users (Username, PasswordHash) VALUES ('admin', 'hashed_password');

...
````

➡️ When you launch the game, you just need to click on the button (white square) to access your database connection : 

<p align="center">
  <img src="pokemon-like/images/img.png" alt="Battle Simulation">
</p>

➡️ Then once you get there :

<p align="center">
  <img src="pokemon-like/images/imgg.png" alt="Battle Simulation">
</p>

You just have to **write** : 

```bash
Server="nameofyourcomputeur"\SQLEXPRESS;Database=ExerciceMonster;Trusted_Connection=True;TrustServerCertificate=True

````

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

## Contact 

[@Tokennn] (https://github.com/Tokennn)

<!-- (Markdown img link) : -->
 

[Git]: https://img.shields.io/badge/Git-grey?style=for-the-badge&logo=git
[Git-url]: https://git-scm.com

[Python]: https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python
[Python-url]: https://www.python.org

 
 
[product-screenshot]: images/screenshot.png
