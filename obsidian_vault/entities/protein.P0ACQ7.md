---
entity_id: "protein.P0ACQ7"
entity_type: "protein"
name: "tdcA"
source_database: "UniProt"
source_id: "P0ACQ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcA b3118 JW3089"
---

# tdcA

`protein.P0ACQ7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACQ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional activator for the tdcABCDE operon. {ECO:0000269|PubMed:8413189}. During anaerobiosis, TdcA participates in controlling genes (tdc operon) involved in transport and metabolism of threonine and serine . Inhibition of tdcA expression by CRISPRi reduced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or pyocyanin . TdcA belongs to the LysR family of transcriptional regulators, and like the other members of this family, it has a helix-turn-helix motif in the N-terminal domain for DNA binding . Although interaction between TdcA and the regulatory region of the tdc operon has not been demonstrated, it has been suggested that TdcA recognizes and binds to an inverted repeat located upstream of the operon . tdcA is the first gene in the tdcABCDEFG operon, which is autoactivated by TdcA. This operon is divergently transcribed with the tdcR gene, whose product also activates the transcription of the operon . TdcA probably interacts with TdcR to activate transcription , and they appear to function together with CRP and IHF, proteins that bend the DNA, for this activation . A mutation in the tdcA gene of enterohemorrhagic Escherichia coli O157:H7 causes the expression of OmpA protein which is involved, among several other processes, in cellular adherence...

## Annotation

FUNCTION: Transcriptional activator for the tdcABCDE operon. {ECO:0000269|PubMed:8413189}.

## Outgoing Edges (7)

- `activates` --> [[gene.b3113|gene.b3113]] `RegulonDB` `S` - regulator=TdcA; target=tdcF; function=+
- `activates` --> [[gene.b3114|gene.b3114]] `RegulonDB` `S` - regulator=TdcA; target=tdcE; function=+
- `activates` --> [[gene.b3115|gene.b3115]] `RegulonDB` `S` - regulator=TdcA; target=tdcD; function=+
- `activates` --> [[gene.b3116|gene.b3116]] `RegulonDB` `S` - regulator=TdcA; target=tdcC; function=+
- `activates` --> [[gene.b3117|gene.b3117]] `RegulonDB` `S` - regulator=TdcA; target=tdcB; function=+
- `activates` --> [[gene.b3118|gene.b3118]] `RegulonDB` `S` - regulator=TdcA; target=tdcA; function=+
- `activates` --> [[gene.b4471|gene.b4471]] `RegulonDB` `S` - regulator=TdcA; target=tdcG; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3118|gene.b3118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACQ7`
- `KEGG:ecj:JW3089;eco:b3118;ecoc:C3026_17005;`
- `GeneID:93778867;947494;`
- `GO:GO:0000987; GO:0003700; GO:0005737; GO:0005829; GO:0006355; GO:0043565; GO:0045893; GO:0070689`

## Notes

HTH-type transcriptional regulator TdcA (Tdc operon transcriptional activator)
