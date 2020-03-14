import java.util.ArrayList;
import java.util.Arrays;

class Hawzen {

    public static void main(String[] args) {
        ArrayList<String[]> arr = new ArrayList<>();
        arr.add(new String[]{"Eiyad", "Abdulrahman", "Osamah","Eiyad"});
        powerSet(arr);
        for (String[] strings : arr) {
            for (String string : strings) {
                System.out.print(string + " ");
            }
            System.out.println();
        }
    }

    public static void powerSet(ArrayList<String[]> arr){
        for (int i = arr.get(0).length; i != 0 ; i--) {
            arr.add(Arrays.copyOfRange(arr.get(0), 0, i -1));
        }
        for (int i = arr.get(0).length - 1; i >= 0; i--) {
            permutation(arr, arr.get(i), 0);
            arr.remove(i);
        }
    }
    /*
    The permutation method works by freezing elements of the array (variables) and swapping the elements.
    ########################################
    #arr: String array ArrayList
    #startIndex: the index of the string array to be permutated
    #arr.get(startIndex).length: number of variables in set
    #freeze: number of variables frozen in set (counting variables on the right to be frozen)
    #arr.get(startIndex).length - freeze: number of variables free (counting free variables from left)

    A set of three variables at the beginning will look like this:
    [free, free, free]
    after one freeze it will look like this:
    [frozen, free, free]
    after all variables are frozen but one it the set will look like this:
    [frozen, frozen, free]

    the function adds the array to the list if it encounters only one free variable.
    */
    public static void permutation(ArrayList<String[]> arr, String[] subArr, int freeze) {
        if (subArr.length - freeze == 1) {
            arr.add(Arrays.copyOf(subArr, subArr.length));
            return;
        }

        for(int i = 0; i < subArr.length - freeze; i++){
            swap(subArr, freeze, freeze+i);
            permutation(arr, subArr, freeze + 1);
            swap(subArr, freeze+i, freeze);
        }
    }

    private static void swap(String[] strings, int a, int b) {
        String temp = strings[a];
        strings[a] = strings[b];
        strings[b] = temp;
    }
}
