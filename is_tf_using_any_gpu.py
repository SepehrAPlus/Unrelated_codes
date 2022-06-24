tf = __import__("tensorflow") #same as import tensorflow as tg
def is_using_gpu() -> bool:
    all_gpus = tf.config.list_physical_devices('GPU')
    number_of_gpus_in_use = all_gpus.__len__()
    output = number_of_gpus_in_use > 0 #checks if ur really using any gpu
    if output == False:
        print("[is_using_gpu] said :You are not using any gpu")
    elif output == True:
        print(f"u are using {number_of_gpus_in_use} number of gpu(s)")
    return output


if "__main__ "== __name__:
    is_using_gpu()
