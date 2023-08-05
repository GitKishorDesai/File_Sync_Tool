#Importing Necessary Modules
import os
import shutil

#Function to Copy the contents of Source Folder in Destination Folder
def mirror_src_and_dest(path_src,path_dest):
    shutil.copytree(path_src,path_dest,dirs_exist_ok=True)

#Function to Delete contents in Destination Folder which are not present in the Source Folder
def delete_in_dest_if_not_in_src(path_src,path_dest):
    if os.path.isdir(path_src) and os.path.isdir(path_dest):
        items_src=set(os.listdir(path_src))
        items_dest=set(os.listdir(path_dest))
        difference=items_dest.difference(items_src)
        if difference:
            for item in difference:
                if os.path.isdir(os.path.join(path_dest,item)):
                    shutil.rmtree(os.path.join(path_dest,item))
                else:
                    os.remove(os.path.join(path_dest,item))
        else:
            for item in items_dest:
                delete_in_dest_if_not_in_src(os.path.join(path_src,item),os.path.join(path_dest,item))
    else:
        pass

#Function which performs the syncing work, i.e., first Mirror the contents of Source Folder in Destination Folder and
# then delete the files in Destination Folder which are not present or were deleted in the Source Folder
def sync(path_src,path_dest):
    mirror_src_and_dest(path_src,path_dest)
    delete_in_dest_if_not_in_src(path_src,path_dest)

#Provision for Future if want to use this code/program as a module in other programs
if __name__=='__main__':
    path_src=''
    path_dest=''
    sync(path_src,path_dest)
