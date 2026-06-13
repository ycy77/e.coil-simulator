---
entity_id: "protein.P38101"
entity_type: "protein"
name: "eamB"
source_database: "UniProt"
source_id: "P38101"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12562784, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eamB yfiK b2578 JW2562"
---

# eamB

`protein.P38101`

## Static

- Type: `protein`
- Source: `UniProt:P38101`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12562784, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Exporter of O-acetylserine (OAS) and cysteine. {ECO:0000269|PubMed:12562784}. EamB (formerly YfiK) is an integral membrane protein . In a strain that is insensitive to feedback inhibition by L-cysteine, overexpression of eamB causes accumulation of L-cysteine and O-acetylserine in the culture medium; overexpression of eamB counteracts the toxicity associated with increased levels of O-acetylserine and increases resistance to the glutamine antagonist, L-AZASERINE; EamB appears to act independently of EG11639-MONOMER "EamA", an alternate O-acetylserine and cysteine efflux permease; the physiological function of EamB is not clear . In the Transporter Classification Database , EamB is a member of the Resistance to Homoserine/Threonine (RhtB) Family (see also ).

## Biological Role

Catalyzes O-acetyl-L-serine export (reaction.ecocyc.RXN0-1923), L-cysteine export (reaction.ecocyc.RXN0-1924).

## Annotation

FUNCTION: Exporter of O-acetylserine (OAS) and cysteine. {ECO:0000269|PubMed:12562784}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1923|reaction.ecocyc.RXN0-1923]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1924|reaction.ecocyc.RXN0-1924]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2578|gene.b2578]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38101`
- `KEGG:ecj:JW2562;eco:b2578;ecoc:C3026_14285;`
- `GeneID:93774508;947065;`
- `GO:GO:0005886; GO:0015171; GO:0015562; GO:0033228`

## Notes

Cysteine/O-acetylserine efflux protein
