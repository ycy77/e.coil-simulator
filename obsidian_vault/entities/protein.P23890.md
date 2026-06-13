---
entity_id: "protein.P23890"
entity_type: "protein"
name: "cadC"
source_database: "UniProt"
source_id: "P23890"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24946151, ECO:0000269|PubMed:7830562}; Single-pass membrane protein {ECO:0000269|PubMed:24946151}. Note=Membrane insertion requires the SecA translocase. {ECO:0000269|PubMed:24946151}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cadC b4133 JW4094"
---

# cadC

`protein.P23890`

## Static

- Type: `protein`
- Source: `UniProt:P23890`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24946151, ECO:0000269|PubMed:7830562}; Single-pass membrane protein {ECO:0000269|PubMed:24946151}. Note=Membrane insertion requires the SecA translocase. {ECO:0000269|PubMed:24946151}.

## Enriched Summary

FUNCTION: Regulates the lysine- and pH-dependent expression of the lysine decarboxylase CadA and the cadaverine-lysine antiporter CadB (PubMed:1370290, PubMed:16491024, PubMed:18086202, PubMed:21216950). At low external pH, and in the presence of external lysine, CadC activates transcription of the cadBA operon by binding directly to two sites, Cad1 and Cad2, within the cadBA promoter region (Pcad) (PubMed:16491024, PubMed:28432336). Preferentially binds to AT-rich regions within the Cad1 promoter (PubMed:28432336). {ECO:0000269|PubMed:1370290, ECO:0000269|PubMed:16491024, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:21216950, ECO:0000269|PubMed:28432336}. CadC is a metal-sensitive transcriptional activator that regulates the expression of genes involved in cadaverine synthesis and excretion under low external pH and high concentrations of lysine . CadC appears to have a modest role in bacterial triclosan resistance . On the other hand, inhibition of cadC expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or puromycin . Two binding sites for CadC, Cad1 and Cad2, have been determined in the cadBA operon. While Cad1 contains an inverted repeat sequence and has a preference for AT-rich regions , Cad2 lacks either an inverted repeat or a palindromic sequence. Both binding sites are necessary for cadBA activation...

## Annotation

FUNCTION: Regulates the lysine- and pH-dependent expression of the lysine decarboxylase CadA and the cadaverine-lysine antiporter CadB (PubMed:1370290, PubMed:16491024, PubMed:18086202, PubMed:21216950). At low external pH, and in the presence of external lysine, CadC activates transcription of the cadBA operon by binding directly to two sites, Cad1 and Cad2, within the cadBA promoter region (Pcad) (PubMed:16491024, PubMed:28432336). Preferentially binds to AT-rich regions within the Cad1 promoter (PubMed:28432336). {ECO:0000269|PubMed:1370290, ECO:0000269|PubMed:16491024, ECO:0000269|PubMed:18086202, ECO:0000269|PubMed:21216950, ECO:0000269|PubMed:28432336}.

## Outgoing Edges (2)

- `activates` --> [[gene.b4131|gene.b4131]] `RegulonDB` `S` - regulator=CadC; target=cadA; function=+
- `activates` --> [[gene.b4132|gene.b4132]] `RegulonDB` `S` - regulator=CadC; target=cadB; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b4133|gene.b4133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23890`
- `KEGG:ecj:JW4094;eco:b4133;ecoc:C3026_22340;`
- `GeneID:948653;`
- `GO:GO:0000156; GO:0000976; GO:0005829; GO:0005886; GO:0006355; GO:0032993; GO:0042803; GO:0045893`

## Notes

Transcriptional activator CadC (Membrane-integrated pH sensor CadC)
