---
entity_id: "protein.P67660"
entity_type: "protein"
name: "yhaJ"
source_database: "UniProt"
source_id: "P67660"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhaJ b3105 JW3076"
---

# yhaJ

`protein.P67660`

## Static

- Type: `protein`
- Source: `UniProt:P67660`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator, may be partially responsible for expression of neighboring gene dlsT (yhaO) (By similarity). {ECO:0000250|UniProtKB:P67661}. YhaJ is a member of the LysR protein family and contains a helix-turn-helix motif to bind DNA, in its N-terminal domain . It was previously associated with regulation of virulence in an enterohemorrhagic Escherichia coli (EHEC) strain . On the other hand, it was predicted that YhaJ regulates genes related to metabolism . Its capability to bind to the promoter regions of several genes in E. coli and regulate their activity has been demonstrated . YhaJ dosage varied drastically between four evolutionarily distinct E. coli strains, including enterohemorrhagic E. coli (EHEC), uropathogenic E. coli (UPEC), neonatal meningitis E. coli (NMEC), and the nonpathogenic commensal K-12, grown in minimal essential medium (MEM). In contrast, growth in rich medium (LB), which naturally enhances YhaJ expression levels, yielded almost identical expression levels of YhaJ in all strains . Increased YhaJ expression levels between minimal and rich media correlated with an increase in the number of global YhaJ binding sites . The regulatory network of YhaJ is surprisingly heterogenous despite its highly conserved nature across the E. coli phylogeny . This suggests that strain-specific regulatory roles for YhaJ are potentially widespread in E...

## Annotation

FUNCTION: Positive regulator, may be partially responsible for expression of neighboring gene dlsT (yhaO) (By similarity). {ECO:0000250|UniProtKB:P67661}.

## Outgoing Edges (7)

- `activates` --> [[gene.b0802|gene.b0802]] `RegulonDB` `S` - regulator=YhaJ; target=ybiJ; function=+
- `activates` --> [[gene.b1060|gene.b1060]] `RegulonDB` `S` - regulator=YhaJ; target=bssS; function=+
- `activates` --> [[gene.b3039|gene.b3039]] `RegulonDB` `S` - regulator=YhaJ; target=ygiD; function=+
- `activates` --> [[gene.b3101|gene.b3101]] `RegulonDB` `S` - regulator=YhaJ; target=yqjF; function=+
- `activates` --> [[gene.b3106|gene.b3106]] `RegulonDB` `S` - regulator=YhaJ; target=yhaK; function=+
- `activates` --> [[gene.b3107|gene.b3107]] `RegulonDB` `S` - regulator=YhaJ; target=yhaL; function=+
- `activates` --> [[gene.b3439|gene.b3439]] `RegulonDB` `S` - regulator=YhaJ; target=yhhW; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3105|gene.b3105]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67660`
- `KEGG:ecj:JW3076;eco:b3105;ecoc:C3026_16950;`
- `GeneID:75173279;947621;`
- `GO:GO:0000976; GO:0001216; GO:0006355; GO:2000144`

## Notes

Probable HTH-type transcriptional regulator YhaJ
