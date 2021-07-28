import os,shutil,sys

if (len(sys.argv) == 3):
    source_path = sys.argv[1]
    target_path = sys.argv[2]
elif (len(sys.argv) == 4):
    param = sys.argv[1]
    source_path = sys.argv[2]
    target_path = sys.argv[3]
else:
    print("Argument error") 
    sys.exit()
    
if ('param' in locals().keys()):
    parse = param.split("=")
    if(parse[0]=='--include-only'):
        include = parse[1].split(',')
    elif(parse[0]=='--exclude-all'):
        exclude = parse[1].split(',')
    else:
        print("Argument error") 
        sys.exit()
    


if not os.path.exists(target_path):
    os.makedirs(target_path)

if os.path.exists(source_path):
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if ('include' in locals().keys()):
                for suffix in include:
                   if (file.endswith(suffix)):
                        src_file = os.path.join(root, file)
                        shutil.copy(src_file, target_path)
                        print(src_file)
            elif ('exclude' in locals().keys()):
                for suffix in exclude:
                   if (not file.endswith(suffix)):
                        src_file = os.path.join(root, file)
                        shutil.copy(src_file, target_path)
                        print(src_file)
            else:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)

print('copy files finished!')