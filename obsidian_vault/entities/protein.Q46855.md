---
entity_id: "protein.Q46855"
entity_type: "protein"
name: "yqhC"
source_database: "UniProt"
source_id: "Q46855"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqhC b3010 JW5849"
---

# yqhC

`protein.Q46855`

## Static

- Type: `protein`
- Source: `UniProt:Q46855`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that positively regulates the expression of the yqhD-dkgA operon (PubMed:20543070, PubMed:20676725, PubMed:34248896). Acts by binding directly to the promoter region of yqhD (PubMed:20543070). {ECO:0000269|PubMed:20543070, ECO:0000269|PubMed:20676725, ECO:0000269|PubMed:34248896}. The YqhC transcriptional activator directly binds to the promoter region of the yqhD gene, which contains the SoxS-like binding sequence as well as a 24-bp palindrome . YqhC also regulates dkgA expression . The yqhD and dkgA genes encode NADPH-dependent oxidoreductases, and both are involved in furfural reduction . YqhC belongs to the AraC/XylS transcriptional activator family, as it shows 13.6% amino acid identity with AraC . The identity of the intracellular signal for YqhC is yet to be discovered . Closely related bacteria contain yqhC, yqhD, and dkgA orthologs in the same arrangement as in Escherichia coli LY180. On the other hand, orthologs of yqhC are also present in more distantly related Gram-negative bacteria . It is probable that YqhC regulates its own expression, since it is inducible by furfural . By using synthetic gene circuits, it was demonstrated that YqhC can repress gene expression from strong promoters through stabilization of RNA polymerase (RNAP) at specific promoter positions...

## Annotation

FUNCTION: Transcriptional regulator that positively regulates the expression of the yqhD-dkgA operon (PubMed:20543070, PubMed:20676725, PubMed:34248896). Acts by binding directly to the promoter region of yqhD (PubMed:20543070). {ECO:0000269|PubMed:20543070, ECO:0000269|PubMed:20676725, ECO:0000269|PubMed:34248896}.

## Outgoing Edges (2)

- `activates` --> [[gene.b3011|gene.b3011]] `RegulonDB` `S` - regulator=YqhC; target=yqhD; function=+
- `activates` --> [[gene.b3012|gene.b3012]] `RegulonDB` `S` - regulator=YqhC; target=dkgA; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3010|gene.b3010]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46855`
- `KEGG:ecj:JW5849;eco:b3010;`
- `GeneID:947491;`
- `GO:GO:0000987; GO:0001216; GO:0006355; GO:0045893`

## Notes

HTH-type transcriptional regulator YqhC
