---
entity_id: "protein.P36771"
entity_type: "protein"
name: "lrhA"
source_database: "UniProt"
source_id: "P36771"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lrhA genR b2289 JW2284"
---

# lrhA

`protein.P36771`

## Static

- Type: `protein`
- Source: `UniProt:P36771`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Not known, does not seem to act on the proton translocating NADH dehydrogenase genes (nuoA-N) which are part of the lrhA operon. LrhA, "LysR homologue A," regulates the transcription of genes involved in the synthesis of type 1 fimbriae . Indirectly, this protein also regulates the transcription of several genes involved in motility, chemotaxis, and flagellum synthesis by directly controlling the expression of the master regulator FlhDC . On the other hand, LrhA also regulates negatively and partially the translation of rpoS through two mechanisms, one of which is RprA dependent and the other one is RprA independent. RprA is a small RNA that regulates positively the translation of rpoS. Both mechanisms of regulation require the presence of the sRNA chaperone Hfq; therefore, it was suggested that another small RNA, in addition to RprA, that regulates rpoS translation is regulated by LrhA . In a gene expression study during the transition from aerobic to anaerobic conditions, part of the regulatory cascade involving the protein LrhA was analyzed...

## Annotation

FUNCTION: Not known, does not seem to act on the proton translocating NADH dehydrogenase genes (nuoA-N) which are part of the lrhA operon.

## Outgoing Edges (5)

- `activates` --> [[gene.b0076|gene.b0076]] `RegulonDB` `S` - regulator=LrhA; target=leuO; function=+
- `activates` --> [[gene.b2289|gene.b2289]] `RegulonDB` `S` - regulator=LrhA; target=lrhA; function=+
- `activates` --> [[gene.b4313|gene.b4313]] `RegulonDB` `S` - regulator=LrhA; target=fimE; function=+
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=LrhA; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=LrhA; target=flhD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2289|gene.b2289]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36771`
- `KEGG:ecj:JW2284;eco:b2289;ecoc:C3026_12770;`
- `GeneID:75205665;946769;`
- `GO:GO:0000987; GO:0003700; GO:0006351; GO:0006355; GO:0043565; GO:0045892; GO:0045893`

## Notes

Probable HTH-type transcriptional regulator LrhA
