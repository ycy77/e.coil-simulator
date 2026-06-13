---
entity_id: "protein.P30749"
entity_type: "protein"
name: "moaE"
source_database: "UniProt"
source_id: "P30749"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moaE chlA5 b0785 JW0768"
---

# moaE

`protein.P30749`

## Static

- Type: `protein`
- Source: `UniProt:P30749`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts molybdopterin precursor Z to molybdopterin. This requires the incorporation of two sulfur atoms into precursor Z to generate a dithiolene group. The sulfur is provided by MoaD. Site-directed mutagenesis and in vitro assays of wild-type and mutant MoaE proteins showed that amino acid residues Lys-119, Arg-39 and Lys-126 are critical for molybdopterin synthase activity . Within the MoaDE complex the two MoaE subunits form a central dimer and each of the two MoaD subunits are located at the opposite ends of the dimer . The crystal structure of a homodimeric MoaE deletion mutant in the absence of MoaD was determined at 2.15 Å resolution . In E. coli K-12, moaE, mog (mogA), moaA, moaB, modB, or modC deletion mutants lose the ability to reduce CPD-4544 (tellurate), which could be restored by complementation. Although the E. coli tellurate reductase gene and its product remain uncharacterized, these data suggest that it involves a molybdoenzyme . ΔiscS, ΔtusA and ΔmoaE are hypersensitive to N-hydroxylated base analogs, such as 6-N-hydroxylaminopurine, exhibit a reduced growth rate, and are resistant to chlorate; this phenotype can be suppressed with addition of L-cysteine or sulfide and is likely due to their role in molybdenum cofactor-dependent pathways .

## Biological Role

Component of molybdopterin synthase (complex.ecocyc.CPLX0-2502).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Converts molybdopterin precursor Z to molybdopterin. This requires the incorporation of two sulfur atoms into precursor Z to generate a dithiolene group. The sulfur is provided by MoaD.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2502|complex.ecocyc.CPLX0-2502]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0785|gene.b0785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30749`
- `KEGG:ecj:JW0768;eco:b0785;ecoc:C3026_04975;`
- `GeneID:945399;`
- `GO:GO:0005829; GO:0006777; GO:0030366; GO:0042803; GO:1990140`
- `EC:2.8.1.12`

## Notes

Molybdopterin synthase catalytic subunit (EC 2.8.1.12) (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protein E) (Molybdopterin-converting factor large subunit) (Molybdopterin-converting factor subunit 2)
