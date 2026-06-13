---
entity_id: "protein.P23847"
entity_type: "protein"
name: "dppA"
source_database: "UniProt"
source_id: "P23847"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1702779}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dppA b3544 JW3513"
---

# dppA

`protein.P23847`

## Static

- Type: `protein`
- Source: `UniProt:P23847`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1702779}.

## Enriched Summary

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:10537211, PubMed:1702779, PubMed:7536291). Binds dipeptides and accepts a wide range of side chains, including small neutral, bulky hydrophobic, and positively and negatively charged groups (PubMed:10537211). Tripeptides are poor substrates (PubMed:10537211). DppA alone controls the specificity of the Dpp transporter (PubMed:10537211). In addition, plays a role in chemotaxis toward peptides via interaction with the chemotaxis protein Tap (PubMed:3520334, PubMed:8563629). {ECO:0000269|PubMed:10537211, ECO:0000269|PubMed:1702779, ECO:0000269|PubMed:3520334, ECO:0000269|PubMed:7536291, ECO:0000269|PubMed:8563629}.; FUNCTION: Binds heme. When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. DppA is the periplasmic binding protein of a dipeptide ABC transport system. dppA mutation results in the inability of a proline auxotroph to utilize Pro-Gly as a proline source; DppA accumulates to high levels when E. coli K-12 strain JM101 is grown in minimal medium; osmotic shock treatment releases DppA into the supernatant...

## Biological Role

Component of dipeptide ABC transporter (complex.ecocyc.ABC-8-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:10537211, PubMed:1702779, PubMed:7536291). Binds dipeptides and accepts a wide range of side chains, including small neutral, bulky hydrophobic, and positively and negatively charged groups (PubMed:10537211). Tripeptides are poor substrates (PubMed:10537211). DppA alone controls the specificity of the Dpp transporter (PubMed:10537211). In addition, plays a role in chemotaxis toward peptides via interaction with the chemotaxis protein Tap (PubMed:3520334, PubMed:8563629). {ECO:0000269|PubMed:10537211, ECO:0000269|PubMed:1702779, ECO:0000269|PubMed:3520334, ECO:0000269|PubMed:7536291, ECO:0000269|PubMed:8563629}.; FUNCTION: Binds heme. When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-8-CPLX|complex.ecocyc.ABC-8-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3544|gene.b3544]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23847`
- `KEGG:ecj:JW3513;eco:b3544;ecoc:C3026_19210;`
- `GeneID:75173738;75201993;948062;`
- `GO:GO:0015031; GO:0015886; GO:0016020; GO:0020037; GO:0030288; GO:0035351; GO:0042277; GO:0042938; GO:0050918; GO:0055052; GO:0071916; GO:1904680`

## Notes

Dipeptide-binding protein (DBP) (Periplasmic dipeptide transport protein)
