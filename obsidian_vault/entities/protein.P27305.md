---
entity_id: "protein.P27305"
entity_type: "protein"
name: "gluQ"
source_database: "UniProt"
source_id: "P27305"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gluQ yadB b0144 JW5892"
---

# gluQ

`protein.P27305`

## Static

- Type: `protein`
- Source: `UniProt:P27305`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the tRNA-independent activation of glutamate in presence of ATP and the subsequent transfer of glutamate onto tRNA(Asp). Glutamate is transferred on the 2-amino-5-(4,5-dihydroxy-2-cyclopenten-1-yl) moiety of the queuosine in position 34 of the tRNA(Asp), the wobble position of the QUC anticodon. Does not transfer glutamate to either tRNA(Glu) or tRNA(Gln). The incapacity of the glutamylated tRNA(Asp) to bind elongation factor Tu suggests that it is not involved in ribosomal protein biosynthesis. {ECO:0000269|PubMed:15096594, ECO:0000269|PubMed:15096612, ECO:0000269|PubMed:15150343}. Glutamyl-Q tRNAAsp synthetase (Glu-Q-RS, GluQ) catalyzes the addition of a glutamate residue to the queosine-modified wobble base of tRNAAsp. The GluQ protein shows similarity to the amino terminal part of bacterial glutamyl-tRNA synthetases, although it lacks the tRNA anticodon interaction domain . The protein is not capable of using tRNAGlu or tRNAGln as a substrate in vitro or in vivo, but can modify tRNAAsp with glutamate . There, glutamate is not esterified to the 3' terminal adenosine, but the 2-amino-5-(4,5-dihydroxy-2-cyclopenten-1-yl) moiety of queosine, which occupies the wobble position of the tRNAAsp anticodon . This tRNA modification is present in the normal E. coli tRNA pool...

## Biological Role

Catalyzes tRNA-queuosine glutamyltransferase (reaction.ecocyc.RXN0-5422).

## Annotation

FUNCTION: Catalyzes the tRNA-independent activation of glutamate in presence of ATP and the subsequent transfer of glutamate onto tRNA(Asp). Glutamate is transferred on the 2-amino-5-(4,5-dihydroxy-2-cyclopenten-1-yl) moiety of the queuosine in position 34 of the tRNA(Asp), the wobble position of the QUC anticodon. Does not transfer glutamate to either tRNA(Glu) or tRNA(Gln). The incapacity of the glutamylated tRNA(Asp) to bind elongation factor Tu suggests that it is not involved in ribosomal protein biosynthesis. {ECO:0000269|PubMed:15096594, ECO:0000269|PubMed:15096612, ECO:0000269|PubMed:15150343}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5422|reaction.ecocyc.RXN0-5422]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0144|gene.b0144]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27305`
- `KEGG:ecj:JW5892;eco:b0144;`
- `GeneID:944846;`
- `GO:GO:0002097; GO:0004818; GO:0005524; GO:0005829; GO:0006424; GO:0008270`
- `EC:6.1.1.-`

## Notes

Glutamyl-Q tRNA(Asp) synthetase (Glu-Q-RSs) (EC 6.1.1.-)
