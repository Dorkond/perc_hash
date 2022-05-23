import imagehash
from PIL import Image
import os
import sys
import time

def find_similar_images(userpaths, hashfunc=imagehash.average_hash):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
               f.endswith(".jpeg") or f.endswith(".bmp") or \
               f.endswith(".gif") or '.jpg' in f or f.endswith(".svg")

    image_filenames = []

    #for userpath in userpaths:
    image_filenames += [os.path.join('d:', os.sep, userpaths, path) for path in os.listdir(userpaths) if is_image(path)]
    images = {}
    for img in sorted(image_filenames):
        try:
            hash = hashfunc(Image.open(img))
        except Exception as e:
            print('Problem:', e, 'with', img)
            continue
        if hash in images:
            print(img, '  already exists as', ' '.join(images[hash]))
            if 'dupPictures' in img:
                print('rm -v', img)
        images[hash] = images.get(hash, []) + [img]


def get_stat(userpaths, hashfunc=imagehash.average_hash, deviation = 0, collision = 0):

    # TEST 1
    def is_test_psnr_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_psnr_10.bmp' or f == str(num) + '_psnr_20.bmp' or \
            f == str(num) + '_psnr_30.bmp' or f == str(num) + '_psnr_40.bmp' or f == str(num) + '_psnr_50.bmp':
            return 1

    # TEST 2
    def is_test_psnr_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_psnr_60.bmp' or f == str(num) + '_psnr_70.bmp' or f == str(num) + '_psnr_80.bmp' or \
            f == str(num) + '_psnr_90.bmp' or f == str(num) + '_psnr_100.bmp':
            return 1

    # TEST 3
    def is_test_noise_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_noise_3.bmp' or f == str(num) + '_noise_6.bmp':
            return 1

    # TEST 4
    def is_test_noise_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_noise_9.bmp' or f == str(num) + '_noise_12.bmp' or f == str(num) + '_noise_15.bmp':
            return 1

    # TEST 5
    def is_test_jpeg_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_jpeg_10.bmp' or f == str(num) + '_jpeg_20.bmp' or f == str(num) + '_jpeg_30.bmp' or \
            f == str(num) + '_jpeg_40.bmp' or f == str(num) + '_jpeg_50.bmp':
            return 1

    # TEST 6
    def is_test_jpeg_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_jpeg_60.bmp' or f == str(num) + '_jpeg_70.bmp' or f == str(num) + '_jpeg_80.bmp' or \
            f == str(num) + '_jpeg_90.bmp' or f == str(num) + '_jpeg_100.bmp':
            return 1

    # TEST 7
    def is_test_median_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_median_3.bmp' or f == str(num) + '_median_5.bmp':
            return 1

    # TEST 8
    def is_test_median_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_median_7.bmp' or f == str(num) + '_median_9.bmp':
            return 1

    # TEST 9
    def is_test_conv(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_conv_1.bmp':
            return 1

    # TEST 10
    def is_test_rml_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rml_10.bmp' or f == str(num) + '_rml_30.bmp':
            return 1

    # TEST 11
    def is_test_rml_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rml_50.bmp' or f == str(num) + '_rml_70.bmp':
            return 1

    # TEST 12
    def is_test_crop_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_crop_45.bmp' or f == str(num) + '_crop_60.bmp' or f == str(num) + '_crop_75.bmp':
            return 1

    # TEST 13
    def is_test_crop_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_crop_85.bmp' or f == str(num) + '_crop_90.bmp' or f == str(num) + '_crop_95.bmp':
            return 1

    # TEST 14
    def is_test_rescale_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_resc_50.bmp' or f == str(num) + '_resc_75.bmp' or f == str(num) + '_resc_90.bmp':
            return 1

    # TEST 15
    def is_test_rescale_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_resc_110.bmp' or f == str(num) + '_resc_150.bmp' or f == str(num) + '_resc_200.bmp':
            return 1

    # TEST 16
    def is_test_rot_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rot_0.5.bmp' or f == str(num) + '_rot_-0.5.bmp' or f == str(num) + '_rot_0.25.bmp' or \
            f == str(num) + '_rot_-0.25.bmp':
            return 1

    # TEST 17
    def is_test_rot_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rot_0.75.bmp' or f == str(num) + '_rot_1.bmp' or f == str(num) + '_rot_2.bmp' or \
                f == str(num) + '_rot_-0.75.bmp' or f == str(num) + '_rot_-1.bmp' or f == str(num) + '_rot_-2.bmp':
            return 1

    # TEST 18
    def is_test_rot_3(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rot_5.bmp' or f == str(num) + '_rot_10.bmp' or f == str(num) + '_rot_15.bmp':
            return 1

    # TEST 19
    def is_test_rot_4(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rot_30.bmp' or f == str(num) + '_rot_45.bmp' or f == str(num) + '_rot_90.bmp':
            return 1

    # TEST 20
    def is_test_rotcrop_1(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rotcrop_0.5.bmp' or f == str(num) + '_rotcrop_0.25.bmp' or \
            f == str(num) + '_rotcrop_-0.5.bmp' or f == str(num) + '_rotcrop_-0.25.bmp':
            return 1

    # TEST 21
    def is_test_rotcrop_2(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_rotcrop_0.75.bmp' or f == str(num) + '_rotcrop_-0.75.bmp' or \
            f == str(num) + '_rotcrop_1.bmp' or f == str(num) + '_rotcrop_-1.bmp' or \
            f == str(num) + '_rotcrop_2.bmp' or f == str(num) + '_rotcrop_-2.bmp':
            return 1

    # TEST 22
    def is_test_affine(filename, num_of_testimg):
        num = int(num_of_testimg)
        f = filename.lower()
        if f == str(num) + '_affine_1.bmp' or f == str(num) + '_affine_2.bmp' or f == str(num) + '_affine_3.bmp' or \
            f == str(num) + '_affine_4.bmp' or f == str(num) + '_affine_5.bmp' or f == str(num) + '_affine_6.bmp' or \
            f == str(num) + '_affine_7.bmp' or f == str(num) + '_affine_8.bmp':
            return 1

    # Number of test images for each test for each image:
    tests_dict = {
        is_test_psnr_1: 5,
        is_test_psnr_2: 5,
        is_test_noise_1: 2,
        is_test_noise_2: 3,
        is_test_jpeg_1: 5,
        is_test_jpeg_2: 5,
        is_test_median_1: 2,
        is_test_median_2: 2,
        is_test_conv: 1,
        is_test_rml_1: 2,
        is_test_rml_2: 2,
        is_test_crop_1: 3,
        is_test_crop_2: 3,
        is_test_rescale_1: 3,
        is_test_rescale_2: 3,
        is_test_rot_1: 4,
        is_test_rot_2: 6,
        is_test_rot_3: 3,
        is_test_rot_4: 3,
        is_test_rotcrop_1: 4,
        is_test_rotcrop_2: 6,
        is_test_affine: 8
    }

    tests_list = [
        is_test_psnr_1,
        is_test_psnr_2,
        is_test_noise_1,
        is_test_noise_2,
        is_test_jpeg_1,
        is_test_jpeg_2,
        is_test_median_1,
        is_test_median_2,
        is_test_conv,
        is_test_rml_1,
        is_test_rml_2,
        is_test_crop_1,
        is_test_crop_2,
        is_test_rescale_1,
        is_test_rescale_2,
        is_test_rot_1,
        is_test_rot_2,
        is_test_rot_3,
        is_test_rot_4,
        is_test_rotcrop_1,
        is_test_rotcrop_2,
        is_test_affine
    ]

    # When you change datasets consider changing str in dataset_origs (2x), deviation !=, and in input function
    # When changing, consider changing split param to match the nesting of new directory
    print('///////////////////////////////////////////////////////////////////////////////////')
    print('Gathering statistics:...')
    print('USING HASH FUNCTION: ' + str(hashfunc))

    #Hashfunc timer
    hash_start = time.time()*1000.0

    # Builds a list of paths to original images
    dataset_origs = ['D:\\AAA\\AAA\\AAA\\0.bmp']
    dataset_origs += [os.path.join('D:\VKR\safecopy\dataset_250_origs', path) for path in os.listdir('D:\VKR\safecopy\dataset_250_origs')]
    dataset_length = len(dataset_origs)
    dataset_origs.sort(key = lambda x: int(x.split('\\')[4].replace('.bmp', '')))
    # print(dataset_origs)
    # Generates dict for imagepath:key values
    hash_dict = {}
    matches = 0
    for is_test in tests_list:
        # Time for test
        test_start = time.time()*1000.0
        counter = 0
        for dataset_image in range(1, dataset_length):
            hash_orig = hashfunc(Image.open('D:\VKR\safecopy\dataset_250_origs' + '/' + str(dataset_image) + '.bmp'))
            # print('calculating original hash for image: ' + 'D:/VKR/dataset_origs' + '/' + str(dataset_image) + '.bmp')
            # print('original hash: ' + str(hash_orig))
            image_filenames = []
            image_filenames += [os.path.join('d:', os.sep, userpaths, path) for path in os.listdir(userpaths) if
                                is_test(path, dataset_image)]
            # print('test hashes')
            for testing_image in image_filenames:
                # print(testing_image)
                hash = hashfunc(Image.open(testing_image))
                hash_dict[testing_image] = hash
                # print('test hash for image: ' + str(hash))
                if hash == hash_orig:
                    counter += 1
        matches += counter
        test_end = time.time()*1000.0
        print('Test: ' + str(is_test) + ' Time took: ' + str(round(test_end - test_start)) + 'ms' + ' Matches: ' + str(counter) + ' ' + 'Possible matches: ' + str((dataset_length-1) * tests_dict[is_test]) + \
              ' ' + 'Percentage: ' + str(round(( counter / ((dataset_length-1) * tests_dict[is_test])), 4)))

    hash_end = time.time()*1000.0
    print('Hashfunc execute time on dataset of ' + str(dataset_length-1) + ' is ' + str(round(hash_end - hash_start, 2)) + ' ms, Average time per image is ' + str(round( (hash_end - hash_start) / ((dataset_length-1) * 80), 2)) + 'ms')
    print('General matches w/ hashfunc: ' + str(matches) + ' General percentage of hashfunc over dataset: ' + str(round(matches / ((dataset_length-1) * 80), 2)))

    if deviation != 0:
        print('Deviation is not null, building result directory tree: ')
        names_for_folders = ['0.bmp']
        names_for_folders_dum = os.listdir('D:\VKR\dataset_50_origs')
        names_for_folders_dum.sort(key = lambda x: int(x.replace('.bmp', '')))
        names_for_folders = names_for_folders + names_for_folders_dum
        print(names_for_folders)
        # for ind in os.listdir('D:\VKR\dataset_origs'):
        #     names_for_folders.append(ind)

        k = 0 # Global counter

        for orig_image_name in names_for_folders:
            # Creates path for result images
            if orig_image_name != '0.bmp':
                # print(orig_image_name)
                path = os.path.join(r'D:\VKR\result', str(hashfunc).replace('<', '').replace('>', '').replace(' ', ''), orig_image_name)
                # path = r'D:\VKR\result\' + str(orig_image_name)
                # print(path)
                print('Directory for image' + str(orig_image_name) + ' created.')
                os.makedirs(path)
                # Creates directories for each deviation:
                for diff in range(3, deviation, 3):
                    path_diff = os.path.join(r'D:\VKR\result' + '/' + str(hashfunc).replace('<', '').replace('>', '').replace(' ', '') + '/' + str(orig_image_name) + '/',  'div_' + str(diff))
                    os.makedirs(path_diff)
                    for key in hash_dict:
                        # print(key, '->', hash_dict[key])
                        # print(dataset_origs[k])
                        # print(hashfunc[dataset_origs[k]])
                        temphash = hashfunc(Image.open(dataset_origs[k]))
                        # print(hash_dict[key] - temphash)
                        # print('Image: ' + str(orig_image_name) + ' Path: ' + str(dataset_origs[k]) + ' diff: ' + str(diff))
                        if hash_dict[key] - hashfunc(Image.open(dataset_origs[k])) <= diff:
                            # print(key)
                            # print(key[20:])
                            # print(path_diff)
                            img = Image.open(key)
                            img.save(path_diff + '/' + key[20:])

            k += 1

    # Dont forget to change split params if you change directory
    if collision != 0:
        colcount = 0
        print('Collision is not null, checking hash collision with hash dictionary')
        for check_img in hash_dict:
            for targ_img in hash_dict:
                if hash_dict[check_img] == hash_dict[targ_img] and check_img.split('\\')[4].split('_')[0] != targ_img.split('\\')[4].split('_')[0] and \
                check_img != targ_img:
                    colcount += 1
                    # print('Collision: ' + str(check_img) + ' with ' + str(targ_img))
        print('Collisions found: ' + str(colcount) + ', % relative to dataset: ' + str(round(colcount / ((dataset_length-1) * 80), 3)))





    #     for dev in range(1, deviation):
    #         #create folder for deviation with original hashname
    #         #for all files in dataset folder:
    #         if hash-hash_orig == dev:
    #             str('lol')
    #             #write files into hashname folder
    # print(tests_dict[is_test])



    # image_filenames += [os.path.join('d:', os.sep, userpaths, path) for path in os.listdir(userpaths) if is_test_psnr(path, 1)]
    # print(image_filenames)
    # images = {}
    # for img in sorted(image_filenames):
    #     try:
    #         hash = hashfunc(Image.open(img))
    #     except Exception as e:
    #         print('Problem:', e, 'with', img)
    #         continue
    #     if hash in images:
    #         print(img, '  already exists as', ' '.join(images[hash]))
    #         if 'dupPictures' in img:
    #             print('rm -v', img)
    #     images[hash] = images.get(hash, []) + [img]

hash_methods = [
imagehash.average_hash,
imagehash.phash,
imagehash.dhash,
imagehash.whash,
imagehash.colorhash,
imagehash.crop_resistant_hash
]

for func in hash_methods:
    get_stat('D:\VKR\safecopy\dataset_250', func, collision = 1)