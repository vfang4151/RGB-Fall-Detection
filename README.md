# RGB-Fall-Detection
RGB Video-Based Fall Detecion Using Deep Learning

To extract skeleton from image
> python3 -m openpifpaf.predict fall-01-cam0-rgb-100.png --json-out

To display the skeleton
> python3 plot_file.py fall-01-cam0-rgb-101.png.predictions.json

To extract skeletons from video
> python3 -m openpifpaf.video --source adl-01-cam0.mp4 --json-out

To display the skeleton animation
> python3 plot_anim.py fall-01-cam0.mp4.openpifpaf.json

Note that there are two persons in fall-13,14

ur-fall-json.tar.gz: skeleton data extracted from ur-fall dataset
