---
entity_id: "protein.P0A6L4"
entity_type: "protein"
name: "nanA"
source_database: "UniProt"
source_id: "P0A6L4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanA npl b3225 JW3194"
---

# nanA

`protein.P0A6L4`

## Static

- Type: `protein`
- Source: `UniProt:P0A6L4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible aldol cleavage of N-acetylneuraminic acid (sialic acid; Neu5Ac) to form pyruvate and N-acetylmannosamine (ManNAc) via a Schiff base intermediate (PubMed:12711733, PubMed:1646603, PubMed:24521460, PubMed:33895133). Experiments show the true substrate is aceneuramate (linearized Neu5Ac), which forms spontaneously at alkaline pH (PubMed:33895133). Linear aceneuramate can be provided by NanQ (PubMed:33895133). Can also cleave other substrates such as N-glycollylneuraminic acid (GcNeu), but not colominic acid or 2-oxocarboxylic acids such as 2-oxohexanoic acid, 2-oxo-octanoic acid, 2-oxo-3-deoxyoctanoic acid and 2-oxononanoic acid (PubMed:1646603). {ECO:0000269|PubMed:12711733, ECO:0000269|PubMed:1646603, ECO:0000269|PubMed:24521460, ECO:0000269|PubMed:33895133}. N-acetylneuraminate lyase (NanA) is part of the PWY0-1324 pathway, where it catalyzes the formation of N-acetylmannosamine and pyruvate from the linear (aldehydo) form of N-acetylneuraminate (NeuNAc) . The enzyme is classified as a Schiff base-forming Class I aldolase . NeuNAc, the substrate of NanA, exists predominantly in the β-anomeric (cyclic) form in solution . Spontaneous mutarotation is slower at low pH . Addition of the NeuNAc anomerases NanM or NanQ to the in vitro assay performed at low pH stimulates NanA activity...

## Biological Role

Component of N-acetylneuraminate lyase (complex.ecocyc.ACNEULY-CPLX).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible aldol cleavage of N-acetylneuraminic acid (sialic acid; Neu5Ac) to form pyruvate and N-acetylmannosamine (ManNAc) via a Schiff base intermediate (PubMed:12711733, PubMed:1646603, PubMed:24521460, PubMed:33895133). Experiments show the true substrate is aceneuramate (linearized Neu5Ac), which forms spontaneously at alkaline pH (PubMed:33895133). Linear aceneuramate can be provided by NanQ (PubMed:33895133). Can also cleave other substrates such as N-glycollylneuraminic acid (GcNeu), but not colominic acid or 2-oxocarboxylic acids such as 2-oxohexanoic acid, 2-oxo-octanoic acid, 2-oxo-3-deoxyoctanoic acid and 2-oxononanoic acid (PubMed:1646603). {ECO:0000269|PubMed:12711733, ECO:0000269|PubMed:1646603, ECO:0000269|PubMed:24521460, ECO:0000269|PubMed:33895133}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACNEULY-CPLX|complex.ecocyc.ACNEULY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3225|gene.b3225]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6L4`
- `KEGG:ecj:JW3194;eco:b3225;ecoc:C3026_17545;`
- `GeneID:86862385;93778761;947742;`
- `GO:GO:0005829; GO:0005975; GO:0008747; GO:0019262; GO:0042802; GO:0044010`
- `EC:4.1.3.3`

## Notes

N-acetylneuraminate lyase (AcNeu lyase) (NAL) (Neu5Ac lyase) (EC 4.1.3.3) (N-acetylneuraminate pyruvate-lyase) (N-acetylneuraminic acid aldolase) (NALase) (Sialate lyase) (Sialic acid aldolase) (Sialic acid lyase)
