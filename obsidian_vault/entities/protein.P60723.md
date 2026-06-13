---
entity_id: "protein.P60723"
entity_type: "protein"
name: "rplD"
source_database: "UniProt"
source_id: "P60723"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplD eryA b3319 JW3281"
---

# rplD

`protein.P60723`

## Static

- Type: `protein`
- Source: `UniProt:P60723`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, this protein initially binds near the 5'-end of the 23S rRNA (PubMed:3298242). It is important during the early stages of 50S assembly (PubMed:3298242). It makes multiple contacts with different domains of the 23S rRNA in the assembled 50S subunit and ribosome (PubMed:6170935, PubMed:7556101). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:2442760, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6170935, ECO:0000269|PubMed:7556101}.; FUNCTION: Protein uL4 is a both a transcriptional repressor and a translational repressor protein; these two functions are independent of each other. It regulates transcription of the S10 operon (to which uL4 belongs) by causing premature termination of transcription within the S10 leader; termination absolutely requires the NusA protein. uL4 controls the translation of the S10 operon by binding to its mRNA. The regions of uL4 that control regulation (residues 131-210) are different from those required for ribosome assembly (residues 89-103). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:1692593, ECO:0000269|PubMed:2157208, ECO:0000269|PubMed:2442760}.; FUNCTION: Forms part of the polypeptide exit tunnel. {ECO:0000269|PubMed:11511371, ECO:0000269|PubMed:2442760, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, this protein initially binds near the 5'-end of the 23S rRNA (PubMed:3298242). It is important during the early stages of 50S assembly (PubMed:3298242). It makes multiple contacts with different domains of the 23S rRNA in the assembled 50S subunit and ribosome (PubMed:6170935, PubMed:7556101). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:2442760, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6170935, ECO:0000269|PubMed:7556101}.; FUNCTION: Protein uL4 is a both a transcriptional repressor and a translational repressor protein; these two functions are independent of each other. It regulates transcription of the S10 operon (to which uL4 belongs) by causing premature termination of transcription within the S10 leader; termination absolutely requires the NusA protein. uL4 controls the translation of the S10 operon by binding to its mRNA. The regions of uL4 that control regulation (residues 131-210) are different from those required for ribosome assembly (residues 89-103). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:1692593, ECO:0000269|PubMed:2157208, ECO:0000269|PubMed:2442760}.; FUNCTION: Forms part of the polypeptide exit tunnel. {ECO:0000269|PubMed:11511371, ECO:0000269|PubMed:2442760, ECO:0000269|PubMed:34403461, ECO:0000269|PubMed:34504068}.; FUNCTION: Can regulate expression from Citrobacter freundii, Haemophilus influenzae, Morganella morganii, Salmonella typhimurium, Serratia marcescens, Vibrio cholerae and Yersinia enterocolitica (but not Pseudomonas aeruginosa) S10 leaders in vitro. {ECO:0000269|PubMed:10498727}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3708|gene.b3708]] `RegulonDB|EcoCyc` `C` - regulator=RplD; target=tnaA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3319|gene.b3319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60723`
- `KEGG:ecj:JW3281;eco:b3319;ecoc:C3026_18035;`
- `GeneID:947818;99707803;99810684;`
- `GO:GO:0001070; GO:0002181; GO:0003677; GO:0003735; GO:0005737; GO:0005829; GO:0006353; GO:0015934; GO:0017148; GO:0019843; GO:0022625; GO:0030371; GO:0031555; GO:0042255; GO:0045892; GO:0046677; GO:0048027; GO:0060698; GO:2000766`

## Notes

Large ribosomal subunit protein uL4 (50S ribosomal protein L4)
