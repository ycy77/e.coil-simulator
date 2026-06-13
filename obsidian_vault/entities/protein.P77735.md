---
entity_id: "protein.P77735"
entity_type: "protein"
name: "yajO"
source_database: "UniProt"
source_id: "P77735"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yajO b0419 JW0409"
---

# yajO

`protein.P77735`

## Static

- Type: `protein`
- Source: `UniProt:P77735`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of ribulose 5-phosphate (Ru5P) to 1-deoxy-D-xylulose 5-phosphate (DXP), providing a direct route from pentoses to terpenes. May play a role in biosynthesis of DXP under conditions of thiamine starvation. {ECO:0000269|PubMed:25326299}. YajO is able to synthesize 1-deoxy-D-xylulose 5-phosphate (DXP) from ribulose 5-phosphate, providing a novel route from a pentose phosphate to DXP . Overexpression of YajO from a multicopy plasmid leads to resistance to the 4-amino-2-methyl-5-hydroxymethylpyrimidine (HMP) analog bacimethrin. The resistance mechanism is undetermined, but does not involve biosynthesis of HMP ; increased synthesis of DXP, a precursor of thiamine, is one of the possibilities . YajO is similar to the AKR7 family of aldo-keto reductases. Purified YajO showed 2-carboxybenzaldehyde reductase activity, but not methylglyoxal reductase activity . Growth of a yajO gloA double mutant is inhibited by 0.3 mM methylglyoxal, but expression of yajO is not increased in response to methylglyoxal . Overexpression of yajO from a plasmid supports cell viability in the absence of the essential dxs-encoded DXS-MONOMER . Review:

## Biological Role

Catalyzes RXN0-7141 (reaction.ecocyc.RXN0-7141).

## Annotation

FUNCTION: Catalyzes the conversion of ribulose 5-phosphate (Ru5P) to 1-deoxy-D-xylulose 5-phosphate (DXP), providing a direct route from pentoses to terpenes. May play a role in biosynthesis of DXP under conditions of thiamine starvation. {ECO:0000269|PubMed:25326299}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7141|reaction.ecocyc.RXN0-7141]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0419|gene.b0419]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77735`
- `KEGG:ecj:JW0409;eco:b0419;ecoc:C3026_02045;`
- `GeneID:75170437;946903;`
- `GO:GO:0005829; GO:0006772; GO:0016491; GO:1902767`
- `EC:1.1.-.-`

## Notes

1-deoxyxylulose-5-phosphate synthase YajO (EC 1.1.-.-)
