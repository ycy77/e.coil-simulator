---
entity_id: "protein.P27126"
entity_type: "protein"
name: "waaS"
source_database: "UniProt"
source_id: "P27126"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaS rfaS b3629 JW3604"
---

# waaS

`protein.P27126`

## Static

- Type: `protein`
- Source: `UniProt:P27126`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May be necessary for the attachment of a rhamnose to the LPS core by a linkage to the KdoII residue (Probable). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388, PubMed:8444813). {ECO:0000269|PubMed:1385388, ECO:0000269|PubMed:8444813, ECO:0000305|PubMed:9791168}. The lipopolysaccharide of E. coli K-12 consists of two major components: the hydrophobic lipid A moiety inserted into the outer membrane and the phosphorylated core oligosaccharide . E. coli K-12 does not produce O antigen to attach to the LPS core due to a defect in the rfb gene cluster which can be complemented with genes from a second, independent rfb mutant to produce an O16 type O antigen . E. coli K-12 may have two major pathways for LPS biosynthesis. One generates LPS cores suitable for O antigen attachment, and a second generates lipooligosaccharides (LOS) with modifications to the core structure which prevent O antigen attachment . waaS encodes a protein necessary for the attachment of Rha to the LPS core by a linkage to the KDOII residue . WaaS could play a role in an LOS biosynthesis pathway, because waaS mutants do not produce certain unsubstituted core bands . A truncated waaS gene was shown to prevent LPS outer core completion . Reviews:

## Biological Role

Catalyzes RXN0-5129 (reaction.ecocyc.RXN0-5129).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Probably involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May be necessary for the attachment of a rhamnose to the LPS core by a linkage to the KdoII residue (Probable). May also play a role in a lipooligosaccharide (LOS) biosynthesis pathway (PubMed:1385388, PubMed:8444813). {ECO:0000269|PubMed:1385388, ECO:0000269|PubMed:8444813, ECO:0000305|PubMed:9791168}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5129|reaction.ecocyc.RXN0-5129]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3629|gene.b3629]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27126`
- `KEGG:ecj:JW3604;eco:b3629;ecoc:C3026_19670;`
- `GeneID:948151;`
- `GO:GO:0005886; GO:0009244`

## Notes

Lipopolysaccharide core biosynthesis protein WaaS
