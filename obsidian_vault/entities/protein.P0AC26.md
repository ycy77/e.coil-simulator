---
entity_id: "protein.P0AC26"
entity_type: "protein"
name: "nirC"
source_database: "UniProt"
source_id: "P0AC26"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nirC b3367 JW3330"
---

# nirC

`protein.P0AC26`

## Static

- Type: `protein`
- Source: `UniProt:P0AC26`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes nitrite uptake and nitrite export across the cytoplasmic membrane. Is up to 10-fold more active than NarK or NarU in nitrite uptake for subsequent reduction in the cytoplasm by the NirB/NirD nitrite reductase. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:18691156}. NirC, encoded within the 4-gene nir operon , is an inner membrane nitrite channel that contributes to both nitrite uptake and nitrite efflux under anaerobic growth conditions (and see further ). Purified NirC, incorporated into liposomes, is permeable to nitrite, nitrate, and formate; it has low permeability to acetate and is impermeable to ammonium and magnesium cations. A pentameric structure has been modeled . In the Transporter Classification Database, NirC is a member of the Formate-Nitrate Transporter (FNT) family (see also ). Related review:

## Biological Role

Catalyzes TRANS-RXN-137 (reaction.ecocyc.TRANS-RXN-137).

## Annotation

FUNCTION: Catalyzes nitrite uptake and nitrite export across the cytoplasmic membrane. Is up to 10-fold more active than NarK or NarU in nitrite uptake for subsequent reduction in the cytoplasm by the NirB/NirD nitrite reductase. {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:18691156}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-137|reaction.ecocyc.TRANS-RXN-137]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3367|gene.b3367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC26`
- `KEGG:ecj:JW3330;eco:b3367;ecoc:C3026_18285;`
- `GeneID:2847757;75173525;75206311;`
- `GO:GO:0005886; GO:0015113; GO:0015499; GO:0015707; GO:0015724; GO:0042128`

## Notes

Nitrite transporter NirC
