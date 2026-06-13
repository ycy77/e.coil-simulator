---
entity_id: "protein.P46891"
entity_type: "protein"
name: "cof"
source_database: "UniProt"
source_id: "P46891"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cof b0446 JW0436"
---

# cof

`protein.P46891`

## Static

- Type: `protein`
- Source: `UniProt:P46891`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P). Can also hydrolyze other substrates such as MeO-HMP-PP and 4-amino-2-trifluoromethyl 5-hydroxymethylpyrimidine pyrophosphate (CF3-HMP-PP) to give MeO-HMP-P and 4-amino-2-trifluoromethyl-5-hydroxymethylpyrimidine phosphate. This hydrolysis generates resistance to the antibiotics (bacimethrin, CF3-HMP) by reducing the formation of their toxic forms, 2'-methoxythiamin pyrophosphate (MeO-TPP) and CF3-HMP-PP. Also hydrolyzes pyridoxal-phosphate (PLP) and flavin mononucleotide (FMN), and purines (GMP and IMP) as secondary substrates. {ECO:0000255|HAMAP-Rule:MF_01847, ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16990279}. Cof is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. The enzyme is involved in the hydrolysis of HMP-PP, an intermediate in thiamin biosynthesis . In a screen using a variety of compounds, its preferred substrate is pyridoxal phosphate; purine and pyrimidine nucleotides are secondary substrates . Overexpression of Cof from a multicopy plasmid leads to resistance to the HMP (4-amino-2-methyl-5-hydroxymethylpyrimidine) analog bacimethrin (MeO-HMP) .

## Biological Role

Catalyzes 3.1.3.74-RXN (reaction.ecocyc.3.1.3.74-RXN), RXN0-3543 (reaction.ecocyc.RXN0-3543). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P). Can also hydrolyze other substrates such as MeO-HMP-PP and 4-amino-2-trifluoromethyl 5-hydroxymethylpyrimidine pyrophosphate (CF3-HMP-PP) to give MeO-HMP-P and 4-amino-2-trifluoromethyl-5-hydroxymethylpyrimidine phosphate. This hydrolysis generates resistance to the antibiotics (bacimethrin, CF3-HMP) by reducing the formation of their toxic forms, 2'-methoxythiamin pyrophosphate (MeO-TPP) and CF3-HMP-PP. Also hydrolyzes pyridoxal-phosphate (PLP) and flavin mononucleotide (FMN), and purines (GMP and IMP) as secondary substrates. {ECO:0000255|HAMAP-Rule:MF_01847, ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16990279}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.3.1.3.74-RXN|reaction.ecocyc.3.1.3.74-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3543|reaction.ecocyc.RXN0-3543]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0446|gene.b0446]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46891`
- `KEGG:ecj:JW0436;eco:b0446;ecoc:C3026_02185;`
- `GeneID:945089;`
- `GO:GO:0000287; GO:0002145; GO:0009228; GO:0016791; GO:0017001; GO:0017110`
- `EC:3.6.1.-`

## Notes

HMP-PP phosphatase (EC 3.6.1.-)
