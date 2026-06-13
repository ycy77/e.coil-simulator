---
entity_id: "protein.P0AE74"
entity_type: "protein"
name: "citT"
source_database: "UniProt"
source_id: "P0AE74"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citT ybdS b0612 JW0604"
---

# citT

`protein.P0AE74`

## Static

- Type: `protein`
- Source: `UniProt:P0AE74`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Responsible for the uptake of citrate in exchange with the efflux of succinate, fumarate or tartrate. Has a relatively broad specificity for C(4)-dicarboxylates and tricarboxylates (PubMed:9696764). {ECO:0000269|PubMed:9696764}. CitT is a putative citrate/succinate antiporter, with the potential to support citrate uptake under anaerobic conditions. In aerobic conditions, E. coli cannot grow with citrate as a sole carbon and energy source due to a lack of transport (see ). Under anaerobic conditions, citrate can be utilised if an oxidizable cosubstrate is present such as glycerol or glucose. Expression of the cloned citT gene conferred the ability to utilise citrate in aerobic conditions. Whole cell transport assays indicated that CitT mediated exchange of citrate with citrate, succinate, tartrate or fumarate . Since succinate is the end product of citrate fermentation, it seems probable that CitT functions physiologically as a citrate/succinate exchanger in anaerobic conditions . Consistent with this supposition, CitT is a member of the DASS family of di- and tri-carboxylic acid transporters. The citT gene is located in an operon including the genes for citrate lyase.

## Biological Role

Catalyzes citrate:succinate antiport (reaction.ecocyc.TRANS-RXN0-201). Transports Succinate (molecule.C00042).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Responsible for the uptake of citrate in exchange with the efflux of succinate, fumarate or tartrate. Has a relatively broad specificity for C(4)-dicarboxylates and tricarboxylates (PubMed:9696764). {ECO:0000269|PubMed:9696764}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-201|reaction.ecocyc.TRANS-RXN0-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0612|gene.b0612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE74`
- `KEGG:ecj:JW0604;eco:b0612;ecoc:C3026_03060;`
- `GeneID:75170616;75205026;949070;`
- `GO:GO:0005886; GO:0015297`

## Notes

Citrate/succinate antiporter (Citrate carrier) (Citrate transporter)
