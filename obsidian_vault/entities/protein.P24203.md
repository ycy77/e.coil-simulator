---
entity_id: "protein.P24203"
entity_type: "protein"
name: "yjiA"
source_database: "UniProt"
source_id: "P24203"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjiA b4352 JW5790"
---

# yjiA

`protein.P24203`

## Static

- Type: `protein`
- Source: `UniProt:P24203`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Zinc chaperone that directly transfers zinc cofactor to target proteins, thereby activating them (By similarity). Zinc is transferred from the CXCC motif in the GTPase domain to the zinc binding site in target proteins in a process requiring GTP hydrolysis (By similarity). {ECO:0000250|UniProtKB:Q8VEH6}. YjiA belongs to the COG0523 subfamily of G3E NTPases. The apoprotein has low GTPase activity that is inhibited by metal binding . A single metal-binding site within the GTPase domain of YjiA binds the transition metal ions Zn(II), Ni(II) and Co(II) with micromolar affinities. Metal binding induces oligomerization of the protein . A crystal structure of YjiA was determined at 2.4 Å resolution . The protein folds into two distinct domains; the structure of the N-terminal domain suggests the presence of a conserved NTP binding site with specificity for guanine, which was experimentally verified. A GTP-dependent regulatory function is proposed for YjiA . Structural analysis of Zn(II)-bound YjiA shows that the protein binds zinc at four distinct sites, one of which is near the GTPase active site . yjiA expression is induced in response to mitomycin C treatment, which causes DNA damage . The yjiS gene defines the left border of the Immigration Control Region (ICR), and yjiA defines the right border...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: Zinc chaperone that directly transfers zinc cofactor to target proteins, thereby activating them (By similarity). Zinc is transferred from the CXCC motif in the GTPase domain to the zinc binding site in target proteins in a process requiring GTP hydrolysis (By similarity). {ECO:0000250|UniProtKB:Q8VEH6}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4352|gene.b4352]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24203`
- `KEGG:ecj:JW5790;eco:b4352;ecoc:C3026_23510;`
- `GeneID:948882;`
- `GO:GO:0003924; GO:0005525; GO:0005737; GO:0005829; GO:0006974; GO:0042802; GO:0046914`
- `EC:3.6.5.-`

## Notes

Zinc chaperone YjiA (EC 3.6.5.-) (GTP-binding protein YjiA)
