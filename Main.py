from tkinter import *
from tkinter import ttk
import random
from tkinter import Toplevel, Label
from BubbleSort import bubble_sort
from QuickSort import quick_sort
from SelectionSort import selectionSort
from InsertionSort import insertionSort
from BogoSort import bogoSort
from MergeSort import mergeSort
from HeapSort import heapSort
from CountingSort import countingSort

# Initialize the main window
root  = Tk()
root.title('Sorting Algorithm Visualiser')
root.attributes('-fullscreen', True)
root.config(bg='#e63c3c')

data = []

# Function to draw the data on the canvas
def drawData(data, comparisons=0, swaps=0):
    canvas.delete('all')
    canvas_height = 650 
    canvas_width = 1400 
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalized_data = [i/max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 570 

        x1 = (i + 1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="#9df5f4")
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=('new roman', 15, 'italic bold'), fill='orange')

        comparison_text = f"Comparisons: {comparisons}"
        swap_text = f"Swaps: {swaps}"


        canvas.create_text(10, 10, anchor=NW, text=comparison_text, font=('new roman', 15, 'italic bold'), fill='black')
        canvas.create_text(10, 40, anchor=NW, text=swap_text, font=('new roman', 15, 'italic bold'), fill='black')

    root.update_idletasks()

# Function to start the selected sorting algorithm
def StartAlgo():
    global data
    timeTick = speedscale.get() * 0.01
    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
        drawData(data)
        
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Selection Sort':
        selectionSort(data, drawData, timeTick)

    elif algo_menu.get() == 'Insertion Sort':
        insertionSort(data, drawData, timeTick)

    elif algo_menu.get() == 'Bogo Sort':
        bogoSort(data, drawData, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        mergeSort(data, 0, len(data)-1, drawData, timeTick)

    elif algo_menu.get() == 'Heap Sort':
        heapSort(data, drawData, timeTick)

    elif algo_menu.get() == 'Counting Sort':
        countingSort(data, drawData, timeTick)

# Function to generate random data
def Generate():
    global data
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())
    
    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawData(data)

# Function to display information about the selected algorithm
def information():
    info_window = Toplevel(root)
    info_window.title("Algorithm Information")
    info_window.geometry("800x500")
    info_window.config(bg='#9df5f4')

    # Dictionary containing detailed information about each algorithm
    algorithm_info = {
        'Bubble Sort': ("Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted."
                        "\n\nDue to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. In computer graphics, it is popular for its capability to detect a tiny error (like a swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n).  It can also be used in special situations where swapping of only adjacent elements is allowed as it sorts the array by swapping only adjacent elements."
                        "\n\nTime Complexity:\n"
                        "Best Case: O(n)\n"
                        "Average Case: O(n^2)\n"
                        "Worst Case: O(n^2)\n"
                        "\n"
                        "Space Complexity: O(1)"),

        'Selection Sort': ("Selection Sort is a simple comparison-based sorting algorithm. The algorithm divides the input list into two parts: the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty, and the unsorted part is the entire list."
                           "\n\nMainly works as a basis for some more efficient algorithms like Heap Sort. Heap Sort mainly uses Heap Data Structure along with the Selection Sort idea. Used when memory writes (or swaps) are costly for example EEPROM or Flash Memory. When compared to other popular sorting algorithms, it takes relatively less memory writes (or less swaps) for sorting. But Selection sort is not optimal in terms of memory writes, cycle sort even requires lesser memory writes than selection sort."
                           "\n\nTime Complexity:\n"
                           "Best Case: O(n^2)\n"
                           "Average Case: O(n^2)\n"
                           "Worst Case: O(n^2)\n"
                           "\n"
                           "Space Complexity: O(1)"),

        'Quick Sort': ("Quick Sort is an efficient, comparison-based, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot."
                       "\n\nThe key process in quickSort is a partition() . The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and put all smaller elements to the left of the pivot, and all greater elements to the right of the pivot. Partition is done recursively on each side of the pivot after the pivot is placed in its correct position and this finally sorts the array."
                       "\n\nTime Complexity:\n"
                       "Best Case: O(n log n)\n"
                       "Average Case: O(n log n)\n"
                       "Worst Case: O(n^2)\n"
                       "\n"
                       "Space Complexity: O(log n)"),

        'Insertion Sort': ("Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is a stable sorting algorithm, meaning that elements with equal values maintain their relative order in the sorted output."
                           "\n\nInsertion sort is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group."
                           "\n\nTime Complexity:\n"
                           "Best Case: O(n)\n"
                           "Average Case: O(n^2)\n"
                           "Worst Case: O(n^2)\n"
                           "\n"
                           "Space Complexity: O(1)"),

        'Bogo Sort': ("BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or monkey sort is a particularly ineffective algorithm one person can ever imagine. It is based on generate and test paradigm. The algorithm successively generates permutations of its input until it finds one that is sorted.(Wiki) For example, if bogosort is used to sort a deck of cards, it would consist of checking if the deck were in order, and if it were not, one would throw the deck into the air, pick the cards up at random, and repeat the process until the deck is sorted."
                      "\n\nTime Complexity:\n"
                      "Best Case: O(n)\n"
                      "Average Case: O((n+1)!)\n"
                      "Worst Case: O(∞)\n"
                      "\n"
                      "Space Complexity: O(1)"),

        'Merge Sort': ("Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array."
                       "\n\nIn simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted."
                       "\n\nTime Complexity:\n"
                       "Best Case: O(n log n)\n"
                       "Average Case: O(n log n)\n"
                       "Worst Case: O(n log n)\n"
                       "\n"
                       "Space Complexity: O(n)"),

        'Heap Sort': ("Heapsort is a comparison-based sorting algorithm which can be thought of as an implementation of selection sort using the right data structure. Like selection sort, heapsort divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Unlike selection sort, heapsort does not waste time with a linear-time scan of the unsorted region; rather, heap sort maintains the unsorted region in a heap data structure to efficiently find the largest element in each step."
                      "\n\nTime Complexity:\n"
                      "Best Case: O(n log n)\n"
                      "Average Case: O(n log n)\n"
                      "Worst Case: O(n log n)\n"
                      "\n"
                      "Space Complexity: O(1)"),

        'Counting Sort': ("Counting sort is an algorithm for sorting a collection of objects according to keys that are small positive integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum key value and the minimum key value, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items. It is often used as a subroutine in radix sort, another sorting algorithm, which can handle larger keys more efficiently."
                          "\n\nTime Complexity:\n"
                          "Best Case: O(n+k)\n"
                          "Average Case: O(n+k)\n"
                          "Worst Case: O(n+k)\n"
                          "\n"
                          "Space Complexity: O(k)"),
    }

    # Retrieve the information for the selected algorithm
    selected_algo = algo_menu.get()
    info_text = algorithm_info.get(selected_algo, "No information available for the selected algorithm.")

    # Display the information in the new window
    info_label = Label(info_window, text=info_text, wraplength=600, justify=LEFT, font=("new roman", 12, 'italic bold'), fg='black', bg='#9df5f4')
    info_label.pack(pady=20, padx=20)

# Create GUI elements
selected_algorithm = StringVar()

mainlabel = Label(root, text='Algorithm:', font=("new roman", 16, 'italic bold'), bg='#0E6DA5', width=10, fg='black', relief=GROOVE, bd=5)
mainlabel.place(x=50, y=20)

algo_menu = ttk.Combobox(root, width=15, font=('new roman', 19, 'italic bold'), textvariable=selected_algorithm, values=['Bubble Sort','Selection Sort','Quick Sort','Insertion Sort','Bogo Sort','Merge Sort','Heap Sort','Counting Sort'])
algo_menu.place(x=210, y=20)
algo_menu.current(0)

sizevaluelabel = Label(root, text='Size:', font=("new roman", 12, 'italic bold'), bg='#0E6DA5', width=10, fg='black', height=2, relief=GROOVE, bd=5)
sizevaluelabel.place(x=50, y=80)
sizevalue = Scale(root, from_=0, to=50, resolution=1, orient=HORIZONTAL, font=('arial', 14, 'italic bold'), relief=GROOVE, bd=2, width=10)
sizevalue.place(x=180, y=80)

minvaluelabel = Label(root, text='Min Value:', font=("new roman", 12, 'italic bold'), bg='#0E6DA5', width=10, fg='black', height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=350, y=80)
minvalue = Scale(root, from_=0, to=20, resolution=1, orient=HORIZONTAL, font=('arial', 14, 'italic bold'), relief=GROOVE, bd=2, width=10)
minvalue.place(x=480, y=80)

maxvaluelabel = Label(root, text='Max Value:', font=("new roman", 12, 'italic bold'), bg='#0E6DA5', width=10, fg='black', height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=640, y=80)
maxvalue = Scale(root, from_=20, to=100, resolution=1, orient=HORIZONTAL, font=('arial', 14, 'italic bold'), relief=GROOVE, bd=2, width=10)
maxvalue.place(x=770, y=80)

start = Button(root, text='Start', bg='#2DAE9A', font=('arial', 12, 'italic bold'), relief=SUNKEN, activebackground='#05945B', activeforeground='white', bd=5, width=10, command=StartAlgo)
start.place(x=1050, y=20)

random_generate = Button(root, text='Generate', bg='#2DAE9A', font=('arial', 12, 'italic bold'), relief=SUNKEN, activebackground='#05945B', activeforeground='white', bd=5, width=10, command=Generate)
random_generate.place(x=1050, y=80)

speedlabel = Label(root, text='Speed:', font=("new roman", 12, 'italic bold'), bg='#0E6DA5', width=10, fg='black', height=2, relief=GROOVE, bd=5)
speedlabel.place(x=550, y=20)
speedscale = Scale(root, from_=0.1, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL, font=('arial', 14, 'italic bold'), relief=GROOVE, bd=2, width=10)
speedscale.place(x=670, y=20)

exit = Button(root, text='Exit', bg='#2DAE9A', font=('arial', 12, 'italic bold'), relief=SUNKEN, activebackground='#05945B', activeforeground='white', bd=5, width=10, command=root.destroy)
exit.place(x=1300, y=20)

info = Button(root, text='Info', bg='#2DAE9A', font=('arial', 12, 'italic bold'), relief=SUNKEN, activebackground='#05945B', activeforeground='white', bd=5, width=10, command=information)
info.place(x=1300, y=80)

canvas = Canvas(root, width=1400, height=650, bg='white')
canvas.place(x=50, y=150)

root.mainloop()
