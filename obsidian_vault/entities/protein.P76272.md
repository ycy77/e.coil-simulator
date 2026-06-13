---
entity_id: "protein.P76272"
entity_type: "protein"
name: "letB"
source_database: "UniProt"
source_id: "P76272"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28819315}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:32359438}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "letB yebT b1834 JW1823"
---

# letB

`protein.P76272`

## Static

- Type: `protein`
- Source: `UniProt:P76272`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28819315}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:32359438}.

## Enriched Summary

FUNCTION: Forms a tunnel that spans the entire periplasmic space (PubMed:28388411, PubMed:31870848, PubMed:32359438). Is probably involved in the transport of lipids between the inner membrane and the outer membrane through the tunnel (PubMed:28388411, PubMed:31870848, PubMed:32359438). Forms a dynamic tunnel sufficiently long to mediate lipid transport directly between the two membranes without the need for a shuttle protein (PubMed:32359438). Binds phospholipids (PubMed:28388411, PubMed:31870848, PubMed:32359438). Lipids bind inside the tunnel (PubMed:32359438). Required for outer membrane homeostasis (PubMed:28819315). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:28388411, ECO:0000269|PubMed:28819315, ECO:0000269|PubMed:31870848, ECO:0000269|PubMed:32359438}.

## Biological Role

Component of lipophilic envelope spanning tunnel (complex.ecocyc.CPLX0-8551).

## Annotation

FUNCTION: Forms a tunnel that spans the entire periplasmic space (PubMed:28388411, PubMed:31870848, PubMed:32359438). Is probably involved in the transport of lipids between the inner membrane and the outer membrane through the tunnel (PubMed:28388411, PubMed:31870848, PubMed:32359438). Forms a dynamic tunnel sufficiently long to mediate lipid transport directly between the two membranes without the need for a shuttle protein (PubMed:32359438). Binds phospholipids (PubMed:28388411, PubMed:31870848, PubMed:32359438). Lipids bind inside the tunnel (PubMed:32359438). Required for outer membrane homeostasis (PubMed:28819315). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:28388411, ECO:0000269|PubMed:28819315, ECO:0000269|PubMed:31870848, ECO:0000269|PubMed:32359438}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8551|complex.ecocyc.CPLX0-8551]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1834|gene.b1834]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76272`
- `KEGG:ecj:JW1823;eco:b1834;ecoc:C3026_10450;`
- `GeneID:946352;`
- `GO:GO:0005886; GO:0030288; GO:0042802; GO:0061024; GO:0120009`

## Notes

Lipophilic envelope-spanning tunnel protein B (Intermembrane transport protein LetB) (Lipid transporter YebT)
