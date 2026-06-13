---
entity_id: "protein.P69801"
entity_type: "protein"
name: "manY"
source_database: "UniProt"
source_id: "P69801"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00429, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:31209249, ECO:0000269|PubMed:8774730}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00429, ECO:0000269|PubMed:31209249}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "manY pel ptsP b1818 JW1807"
---

# manY

`protein.P69801`

## Static

- Type: `protein`
- Source: `UniProt:P69801`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00429, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:31209249, ECO:0000269|PubMed:8774730}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00429, ECO:0000269|PubMed:31209249}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}. ManY is a hydrophobic integral membrane protein which together with ManZ forms the transmembrane channel of the E. coli ManXYZ mannose permease . ManY contains a PTS Enzyme IIC domain. The ManY and ManZ proteins alone are sufficient for penetration of λ phage DNA . Engineered expression of EG10227-MONOMER "DicB" (encoded on the Qin prophage) inhibits ManYZ-mediated phage uptake and transport of the PTS sugars, mannose and glucosamine; the new phenotypes (phage λ resistance and growth inhibition on plates with mannose or glucosamine as carbon source) are dependent on DicB-MinC interaction . The ManY (and ManZ) structure consists of core, arm and V-motif domains; the core domains form the substrate binding site of a ManYZ protomer .

## Biological Role

Component of mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1818|gene.b1818]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69801`
- `KEGG:ecj:JW1807;eco:b1818;ecoc:C3026_10355;`
- `GeneID:93776067;946332;`
- `GO:GO:0005886; GO:0009401; GO:0015761; GO:0015764; GO:0016020; GO:0022870; GO:0098708; GO:1902495; GO:1990539`

## Notes

PTS system mannose-specific EIIC component (EII-P-Man) (EIIC-Man) (Mannose permease IIC component)
