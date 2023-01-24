public class Selection (Rock)
    prublic static void main (String1] args) ()
        // Computer will randomly choose a move
    }
 }

public class selection {
    public static void main (String[] args) {}
        //moves = ["Rock", "Paper", "Scissors" ]

        //Computer randomly chooses a move
        // maybe a "move" is just an integer that represents one of the choices
        // 1 means "rock", 2 means "paper",  3 means "scissors"

        int computerChoice = 1;

        //Get a move from the user
        // user will enter an integer corresponding to their choice
        // We need to print a message telling them the valid choices
        System.out.print("Enter a move (1 for rock, 2 for papper, 3 for scissors): ");

        Scanner input = new Scanner(System.in);

        int userChoice = input.nextInt();

        //Compare the two moves and decide the winner
        // use if-else statements
        if (userChoice == computerChoice) {
            System.out.print("Draw! You both chose ???");
        }
        // check if computer chose rock
        else if (computerChoice == 1) {
            //if so, then check if user chose paper
            if (userChoice == 2) {}
            //      if so, then user wins (Congratulations, you have won!)
    } else {
            //otherwise, user must habe chosen scissors
            //      so the computer wins (You have lost.)
            }
        }
    }
}