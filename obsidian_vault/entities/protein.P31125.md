---
entity_id: "protein.P31125"
entity_type: "protein"
name: "eamA"
source_database: "UniProt"
source_id: "P31125"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eamA ydeD b1533 JW5250"
---

# eamA

`protein.P31125`

## Static

- Type: `protein`
- Source: `UniProt:P31125`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: May be an export pump for cysteine and other metabolites of the cysteine pathway (such as N-acetyl-L-serine (NAS) and O-acetyl-L-serine (OAS)), and for other amino acids and their metabolites. {ECO:0000269|PubMed:10844694, ECO:0000269|Ref.6}. EamA (formerly YdeD) is an integral membrane protein . EamA is implicated in exporting metabolites of the cysteine pathway; strains overexpressing eamA do not grow on minimal medium with sulfate as the sole sulfur source but do grow when supplemented with L-cystine or with L-methionine plus thiosulfate; strains overexpressing eamA (and grown with L-methionine plus thiosulfate) excrete cysteine, O-acetyl-L-serine and other unidentified compounds* into the culture medium . Overexpression of eamA counteracts the toxicity associated with increased levels of O-acetylserine and increases resistance to the glutamine antagonist, L-AZASERINE; EamA appears to act independently of EG12445-MONOMER "EamB", an alternate O-acetylserine and cysteine efflux permease; EamA may function to modulate O-acetyl-L-serine concentration during exponential growth...

## Biological Role

Catalyzes O-acetyl-L-serine export (reaction.ecocyc.RXN0-1923), L-cysteine export (reaction.ecocyc.RXN0-1924).

## Annotation

FUNCTION: May be an export pump for cysteine and other metabolites of the cysteine pathway (such as N-acetyl-L-serine (NAS) and O-acetyl-L-serine (OAS)), and for other amino acids and their metabolites. {ECO:0000269|PubMed:10844694, ECO:0000269|Ref.6}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1923|reaction.ecocyc.RXN0-1923]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1924|reaction.ecocyc.RXN0-1924]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1533|gene.b1533]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31125`
- `KEGG:ecj:JW5250;eco:b1533;ecoc:C3026_08855;`
- `GeneID:946081;`
- `GO:GO:0005886; GO:0015562; GO:0033228; GO:0070301`

## Notes

Probable amino-acid metabolite efflux pump
