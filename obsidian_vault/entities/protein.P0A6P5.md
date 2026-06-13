---
entity_id: "protein.P0A6P5"
entity_type: "protein"
name: "der"
source_database: "UniProt"
source_id: "P0A6P5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "der engA yfgK b2511 JW5403"
---

# der

`protein.P0A6P5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6P5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: GTPase that plays an essential role in the late steps of ribosome biogenesis. GTPase point mutations (but not a deletion mutant) are suppressed by mild overexpression of RelA, probably due to increased levels of the stringent response mediator (p)ppGpp. 50S subunits assembled in the absence of Der are defective and unable to assemble into 70S ribosomes. GTPase activity is stimulated by YihI. Overexpression rescues an rrmJ deletion, stabilizing the 70S ribosome. Der and RrmJ are likely to share a mechanism to stabilize 50S ribosomal subunits at a very late stage of 50S subunit maturation possibly by interacting with 23S rRNA or 23S rRNA/r-protein complex. {ECO:0000269|PubMed:11976298, ECO:0000269|PubMed:16930151}. The Der protein is a GTPase that is ubiquitously conserved in eubacteria . It is associated with the large ribosomal subunit and is required for its stability . In E. coli, Der is essential for growth . GTP hydrolysis appears to regulate the specificity of interactions of Der with ribosomal subunits . The GAP-like protein CPLX0-7853 "YihI" interacts with Der and activates its GTPase activity . The GTPase activity of Der is also stimulated by the 50S ribosomal subunit . The KH-like C-terminal domain of Der plays a role in recognition of the ribosome . Der also interacts with G6362-MONOMER YbeY and binds (p)ppGpp...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: GTPase that plays an essential role in the late steps of ribosome biogenesis. GTPase point mutations (but not a deletion mutant) are suppressed by mild overexpression of RelA, probably due to increased levels of the stringent response mediator (p)ppGpp. 50S subunits assembled in the absence of Der are defective and unable to assemble into 70S ribosomes. GTPase activity is stimulated by YihI. Overexpression rescues an rrmJ deletion, stabilizing the 70S ribosome. Der and RrmJ are likely to share a mechanism to stabilize 50S ribosomal subunits at a very late stage of 50S subunit maturation possibly by interacting with 23S rRNA or 23S rRNA/r-protein complex. {ECO:0000269|PubMed:11976298, ECO:0000269|PubMed:16930151}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2511|gene.b2511]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6P5`
- `KEGG:ecj:JW5403;eco:b2511;ecoc:C3026_13925;`
- `GeneID:75206204;946983;`
- `GO:GO:0000027; GO:0003924; GO:0005525; GO:0005829; GO:0032794; GO:0043022; GO:0043023; GO:0097216`

## Notes

GTPase Der (Double era-like domain protein) (GTP-binding protein EngA)
