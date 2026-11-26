import gc
import tracemalloc

tracemalloc.start()

print("GC Thresholds:", gc.get_threshold())

def create_reference_cycles(count):
    for i in range(count):
        a = {}
        b = {"ref": a, "data": [j for j in range(1000)]}
        a["ref"] = b  

current_before, peak_before = tracemalloc.get_traced_memory()
print(f"\n[Before Object Creation] Current Memory: {current_before / 1024:.2f} KB")

create_reference_cycles(500)

current_after_alloc, _ = tracemalloc.get_traced_memory()
print(f"[Before Manual GC]       Current Memory: {current_after_alloc / 1024:.2f} KB")

collected_objects = gc.collect()
print(f"\nManual GC executed -> Collected {collected_objects} unreachable objects.")

current_after_gc, peak_after_gc = tracemalloc.get_traced_memory()
print(f"[After Manual GC]        Current Memory: {current_after_gc / 1024:.2f} KB")
print(f"Memory Reclaimed: {(current_after_alloc - current_after_gc) / 1024:.2f} KB")

tracemalloc.stop()