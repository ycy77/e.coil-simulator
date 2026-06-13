---
entity_id: "protein.P37597"
entity_type: "protein"
name: "punC"
source_database: "UniProt"
source_id: "P37597"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "punC ydhC b1660 JW1652"
---

# punC

`protein.P37597`

## Static

- Type: `protein`
- Source: `UniProt:P37597`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Transports purine nucleosides (PubMed:34413462). Shows a broad specificity for purine nuclesides, including adenosine, 2-deoxyadenosine, guanosine and inosine (PubMed:32994326, PubMed:34413462). Uptake of purine nucleosides may support growth under nitrogen-limiting conditions (PubMed:34413462). It also exhibits specificity for the uptake of certain sulfonamides, which are structural analogs of para-aminobenzoic acid (PABA) (PubMed:34413462). Was originally identified as a putative arabinose efflux transporter, however, overexpression of the gene has no effect on intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:22952739, ECO:0000269|PubMed:32994326, ECO:0000269|PubMed:34413462}. PunC is a purine nucleoside transporter that supports growth under nitrogen-limiting conditions; a punC deletion strain from the Keio collection is unable to grow with adenosine or 2-deoxyadenosine as the nitrogen source; the punC mutant also shows a growth defect with inosine or guanosine as nitrogen source . PunC is implicated in the uptake of some sulfonamide antibiotics . PunC is a member of the Drug:H+ Antiporter (DHA) Family within the Major Facilitator Superfamily (MFS) of transporters . PunC is implicated in arabinose efflux...

## Biological Role

Catalyzes TRANS-RXN0-631 (reaction.ecocyc.TRANS-RXN0-631).

## Annotation

FUNCTION: Transports purine nucleosides (PubMed:34413462). Shows a broad specificity for purine nuclesides, including adenosine, 2-deoxyadenosine, guanosine and inosine (PubMed:32994326, PubMed:34413462). Uptake of purine nucleosides may support growth under nitrogen-limiting conditions (PubMed:34413462). It also exhibits specificity for the uptake of certain sulfonamides, which are structural analogs of para-aminobenzoic acid (PABA) (PubMed:34413462). Was originally identified as a putative arabinose efflux transporter, however, overexpression of the gene has no effect on intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:22952739, ECO:0000269|PubMed:32994326, ECO:0000269|PubMed:34413462}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-631|reaction.ecocyc.TRANS-RXN0-631]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1660|gene.b1660]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37597`
- `KEGG:ecj:JW1652;eco:b1660;ecoc:C3026_09525;`
- `GeneID:946077;`
- `GO:GO:0005886; GO:0015211; GO:0015860; GO:0022857; GO:0042910; GO:1990961`

## Notes

Purine nucleoside transporter (Adenosine efflux transporter)
