import numpy as np


def getDlibLandmark(landmark):
    indexes = list(range(0, 17, 2))
    indexes.extend(list(range(17, 60)))
    result = [(landmark.part(i).x, landmark.part(i).y) for i in indexes]
    return np.asarray(result, dtype="double")


def projection_end(point_3d, matrix, camera):
    point_3d = np.append(point_3d, np.ones((len(point_3d), 1)), axis=1).T
    end = camera.dot(matrix.dot(point_3d))
    end = (end / end[2]).T
    return end[:, 0:2]


def dist_bt_2_face(face1, face2):
    face1 = np.asarray(face1)
    face2 = np.asarray(face2)
    plot_count = len(face1)
    dists = face1 - face2
    sum_dist = 0.0
    for dist in dists:
        sum_dist += np.linalg.norm(dist)
    return sum_dist / plot_count
