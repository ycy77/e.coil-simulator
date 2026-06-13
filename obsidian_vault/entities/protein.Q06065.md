---
entity_id: "protein.Q06065"
entity_type: "protein"
name: "atoC"
source_database: "UniProt"
source_id: "Q06065"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16153782}. Note=Membrane-associated in the presence of AtoS. {ECO:0000269|PubMed:16153782}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atoC az b2220 JW2214"
---

# atoC

`protein.Q06065`

## Static

- Type: `protein`
- Source: `UniProt:Q06065`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16153782}. Note=Membrane-associated in the presence of AtoS. {ECO:0000269|PubMed:16153782}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408, PubMed:2883171). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoC acts by binding directly to the promoter region of the target genes (PubMed:17616594). In addition to its role as a transcriptional regulator, functions as a post-translational regulator that inhibits polyamine biosynthesis via regulation of ornithine decarboxylase (ODC) (PubMed:8346225). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:17616594, ECO:0000269|PubMed:22083893, ECO:0000269|PubMed:2883171, ECO:0000269|PubMed:8346225}. AtoC, also known as antizyme protein (Az), is a protein that regulates processes at the transcriptional and posttranslational levels . It inhibits posttranslationally ornithine decarboxylase (ODC) , which is a key enzyme for biosynthesis of the polyamines which are essential components for cellular growth and proliferation...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408, PubMed:2883171). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoC acts by binding directly to the promoter region of the target genes (PubMed:17616594). In addition to its role as a transcriptional regulator, functions as a post-translational regulator that inhibits polyamine biosynthesis via regulation of ornithine decarboxylase (ODC) (PubMed:8346225). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:17616594, ECO:0000269|PubMed:22083893, ECO:0000269|PubMed:2883171, ECO:0000269|PubMed:8346225}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (4)

- `activates` --> [[gene.b2221|gene.b2221]] `RegulonDB` `C` - regulator=AtoC; target=atoD; function=+
- `activates` --> [[gene.b2222|gene.b2222]] `RegulonDB` `C` - regulator=AtoC; target=atoA; function=+
- `activates` --> [[gene.b2223|gene.b2223]] `RegulonDB` `C` - regulator=AtoC; target=atoE; function=+
- `activates` --> [[gene.b2224|gene.b2224]] `RegulonDB` `C` - regulator=AtoC; target=atoB; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2220|gene.b2220]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q06065`
- `KEGG:ecj:JW2214;eco:b2220;ecoc:C3026_12410;`
- `GeneID:947444;`
- `GO:GO:0000160; GO:0000987; GO:0001216; GO:0003700; GO:0005524; GO:0005737; GO:0032993; GO:0045893`

## Notes

Regulatory protein AtoC (Acetoacetate metabolism regulatory protein) (DNA-binding transcriptional regulator AtoC) (Ornithine decarboxylase antizyme)
