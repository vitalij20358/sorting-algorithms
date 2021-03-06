import test, algorithms as alg, file_handling as f_handl, console_handling as cl_handl
from time import time

def Sort(path_in, path_out, algorithm = 's', 
	captions = True, clear_out_f = True, print_info = True, progress_bar = True):
	''' Sort all sequences in the file with path "path_in" and writes it to the file
	 with the path "path_out". 

	 The sorting algorithm can be specified by the "algorithm" parameter:
	 	's', 'S' - selection sort
	 	'h', 'H' - binary heap sort 

	 If captions flag is set then the output sequences will be labeled.

	 "clear_out_f" flag can be turned off not to clear an output file before 
	 writing down the results.

	 If print_info flag is set then some info about the task will be printed
	 to the console.
	'''

	# Reading an input file
	sequences = f_handl.ReadInputFile(path_in)	
	if type(sequences[0]) != list:
		if sequences[0] == -1:
			print("File '{}' exist, but is empty or unreadable.\n Number of misunderstood words: {}".format(
				path_in, sequences[1]))
		elif sequences[0] == -2:
			print('File \'{}\' not found'.format(path_in))
		elif sequences[0] == -3:
			print('Something went wrong while reading file \'{}\''.format(path_in))
		return -1
	else:
		if sequences[1]>0:
			print('Number of misunderstood words:',sequences[1])
		sequences = sequences[0]

	counter = 1
	times = []
	if clear_out_f:
		f_handl.PrepareFile(path_out)	# Clearing the output file

	cl_handl.draw_separator(path_in)

	counter = 0
	for sequence in sequences:

		if algorithm.lower() == 's':
			start_time = time()
			array = alg.SelectionSort(sequence)
			end_time = time()
		elif algorithm.lower() == 'h':
			start_time = time()
			array = alg.BinaryHeapSort(sequence)
			end_time = time()

		times += [round(end_time-start_time, 4)]

		if captions:
			f_handl.AppendFile(path=path_out, out_list=array, label=counter)
		else:
			f_handl.AppendFile(path=path_out, out_list=array, end='\n')

		counter += 1
		if progress_bar:
			cl_handl.update_progress(counter/len(sequences), path_in)

	if print_info:
		print('')
		cl_handl.task_info(len(sequences), times, path_in, path_out, algorithm.lower())

	return times



def demonstrate(generate_data = False):
	''' Implementation of all functions and showing the graph of the results. In other words - examples.'''
	# path="./tests/test.txt"
	
	# Creating an input file for the test
	test.CreateInput(path="./tests/main_test.txt", Nmin = 0, Nmax = 1000, sequences = 100, len_start = 10,
		len_incr = 10, len_mult = 1, complexity = 0)
	
	# Creating an numpy array of the times of algorithm working time
	sel_times = np.array(Sort('./tests/main_test.txt', './tests/sel_result.txt', algorithm = 'S', captions = False))
	heap_times = np.array(Sort('./tests/main_test.txt','./tests/heap_result.txt',algorithm = 'H', captions = False))

	# Values for x axes in numpy array format. Similar to np.array(range(100))
	x = np.linspace(0, 100, 100)

	plt.figure('Algorithms comparison')
	plt.scatter(x, sel_times, s=10, c = 'red',  label = 'Selection Sort')
	plt.scatter(x, heap_times, s=10, c = 'green', label = 'Binary Heap Sort')
	plt.xlabel('Number of numbers')
	plt.ylabel('Time, seconds')
	plt.title('Binary Heap Sort and Selection Sort algorithms comparison')
	plt.legend(loc=2)
	ticks = np.linspace(0, 100, 6)
	tick_labels = np.linspace(10, 1010, 6)
	plt.xticks(ticks=ticks, labels=tick_labels)
	plt.show()
	plt.close()


	n = 100
	s_len = 10000
	s_len_2 = int(s_len/10)
	x = np.linspace(0, n, n)

	print('\nCreating a new set of data...', flush = True)

	test.CreateInput(path="./tests/a_ascending_test.txt", Nmin = 0, Nmax = s_len*5, sequences = n, 
		len_start = s_len, len_incr = 0, len_mult = 1, complexity = -1, distrib = 15, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path="./tests/f_random_test.txt", 	Nmin = 0, Nmax = s_len*5, sequences = n, 
		len_start = s_len, len_incr = 0, len_mult = 1, complexity =  0, distrib = 15, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path="./tests/a_descending_test.txt",Nmin = 0, Nmax = s_len*5, sequences = n, 
		len_start = s_len, len_incr = 0, len_mult = 1, complexity =  1, distrib = 15, dist_incr = 0, dist_mult = 1)

	test.CreateInput(path="./tests/sel_a_asc_test.txt",  Nmin = 0, Nmax = s_len_2*5, sequences = n, 
		len_start = s_len_2, len_incr = 0, len_mult = 1, complexity = -1, distrib = 15, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path="./tests/sel_f_rand_test.txt", Nmin = 0, Nmax = s_len_2*5, sequences = n, 
		len_start = s_len_2, len_incr = 0, len_mult = 1, complexity =  0, distrib = 15, dist_incr = 0, dist_mult = 1)
	test.CreateInput(path="./tests/sel_a_desc_test.txt", Nmin = 0, Nmax = s_len_2*5, sequences = n, 
		len_start = s_len_2, len_incr = 0, len_mult = 1, complexity =  1, distrib = 15, dist_incr = 0, dist_mult = 1)
	

	heap_times_m1 = np.array(Sort('./tests/a_ascending_test.txt','./tests/a_ascending_result.txt',
		algorithm = 'H', captions = False))
	heap_times_0 = np.array(Sort('./tests/f_random_test.txt','./tests/f_random_result.txt',
		algorithm = 'H', captions = False))
	heap_times_1 = np.array(Sort('./tests/a_descending_test.txt','./tests/a_descending_result.txt',
		algorithm = 'H', captions = False))

	sel_times_m1 = np.array(Sort('./tests/sel_a_asc_test.txt','./tests/sel_a_asc_result.txt',
		algorithm = 'S', captions = False))
	sel_times_0= np.array(Sort('./tests/sel_f_rand_test.txt','./tests/sel_f_rand_result.txt',
		algorithm = 'S', captions = False))
	sel_times_1 = np.array(Sort('./tests/sel_a_desc_test.txt','./tests/sel_a_desc_result.txt',
		algorithm = 'S', captions = False))

	plt.figure('Inputs comparison')

	plt.subplot(2,2,1)
	plt.scatter(x, heap_times_m1,s=10, c = 'red',  label = 'almost ascending')
	plt.scatter(x, heap_times_0, s=10, c = 'green',label = 'fully random')
	plt.scatter(x, heap_times_1, s=10, c = 'blue', label = 'almost descending')
	plt.xlabel('Number of test')
	plt.ylabel('Time, seconds')
	plt.title('Binary Heap sorting algorithm')
	plt.legend(loc=2)
	
	plt.subplot(2,2,2)
	plt.scatter(x, sel_times_m1,s=10, c = 'red',  label = 'almost ascending')
	plt.scatter(x, sel_times_0,	s=10, c = 'green',label = 'fully random')
	plt.scatter(x, sel_times_1,	s=10, c = 'blue', label = 'almost descending')
	plt.xlabel('Number of test')
	plt.ylabel('Time, seconds')
	plt.title('Selection sorting algorithm')
	plt.legend(loc=2)

	plt.subplot(2,2,3)
	plt.hist(heap_times_m1, bins=5, color = 'red',  label = 'almost ascending', 	alpha = 0.7)
	plt.hist(heap_times_0,	bins=5, color = 'green',label = 'fully random',	 	alpha = 0.7)
	plt.hist(heap_times_1,	bins=5, color = 'blue', label = 'almost descending',	alpha = 0.7)
	plt.xlabel('Time, seconds')
	plt.ylabel('Number of test')
	
	plt.subplot(2,2,4)
	plt.hist(sel_times_m1,	bins=5, color = 'red',  label = 'almost ascending',  	alpha = 0.5)
	plt.hist(sel_times_0,	bins=5, color = 'green',label = 'fully random', 	  	alpha = 0.5)
	plt.hist(sel_times_1,	bins=5, color = 'blue', label = 'almost descending', 	alpha = 0.5)
	plt.xlabel('Time, seconds')
	plt.ylabel('Number of test')

	plt.show()
	


def main():
	''' Main function '''

	# Initial test
	Sort('./tests/initial_test.txts', './tests/initial_result.txt', algorithm = 'H', 
		captions = True, progress_bar = False)

	# The most important tests are stored in the demonstrate() function
	try:
		import matplotlib.pyplot as plt, numpy as np
		global plt, np
	except ModuleNotFoundError as exc:
		print('\n\n{}\n\nPlease install the module mentioned above\n'.format(exc)+
			'to be able to appreciate some beautiful plots.')
	else:
		demonstrate()

	# If you need the console not to close immediately after
	# finishing your task, then please uncomment the following two rows. 
	# import os 							
	# os.system("pause")


if __name__ == "__main__":
    main()