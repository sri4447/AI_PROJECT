# Implementation Of Baroque Chess

## Overview
This Python module provides a Baroque Chess agent capable of playing a game of Baroque Chess using the minimax algorithm with alpha-beta pruning. Baroque Chess is a chess variant with unique rules that add complexity to the game.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Feature](#Feature)
- [Discription](#Discription)
- [Customization](#customization)
- [Contributing](#contributing)

### Introduction

- Baroque Chess is a variant of chess that introduces unconventional pieces and changes to the standard chess rules. This project implements a Baroque Chess agent with a basic evaluation function and the alpha-beta pruning algorithm to make optimal moves.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sri4447/AI_PROJECT/edit/main/README.MD
   cd baroque-chess-agent

## Usage

1. Install the required libraries:

   <pre>
     pip install python-chess
   </pre>

## Features

Minimax algorithm with alpha-beta pruning.
Basic evaluation function for piece values.
Interactive gameplay against the Baroque Chess agent.

## Discription

This code includes a more advanced BaroqueChessAgent class that uses the minimax algorithm with alpha-beta pruning for move generation. The evaluate_board function provides a simple evaluation of the board based on material balance. Adjustments and enhancements can be made to improve the evaluation function and the overall performance of the agent. Additionally, the play_tournament function allows multiple agents to compete against each other in a specified number of rounds.

Initialization: The init method initializes the agent with the board state, color, and maximum search depth.

Evaluation Function: The evaluate_board method evaluates the current board position based on piece values.

Minimax with Alpha-Beta Pruning: The minimax and alpha_beta_pruning methods implement the Minimax algorithm with alpha-beta pruning. These methods consider possible future moves and select the best move based on the evaluation function.

Make Move: The make_move method selects the best move for the current player using the alpha-beta pruning algorithm.

Play: The play method simulates the gameplay, making moves for the agent until the game is over.

Tournament: The play_tournament function allows multiple agents to compete against each other in a specified number of rounds, keeping track of their scores.

## Customization

You can customize the Baroque Chess Agent by adjusting the depth of the minimax search and refining the evaluation function. Explore the code in file1.py to understand and modify the behavior.

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or create a pull request. Contributions are welcome!


