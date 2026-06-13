---
entity_id: "gene.b2296"
entity_type: "gene"
name: "ackA"
source_database: "NCBI RefSeq"
source_id: "gene-b2296"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2296"
  - "ackA"
---

# ackA

`gene.b2296`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2296`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ackA (gene.b2296) is a gene entity. It encodes ackA (protein.P0A6A3). Encoded protein function: FUNCTION: Catalyzes the formation of acetyl phosphate from acetate and ATP. Can also catalyze the reverse reaction. During anaerobic growth of the organism, this enzyme is also involved in the synthesis of most of the ATP formed catabolically. The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:16080684}. EcoCyc product frame: ACETATEKINA-MONOMER. Genomic coordinates: 2413470-2414672. EcoCyc protein note: AckA has propionate kinase activity as well as acetate kinase activity. The ackA-encoded propionate kinase 2 has an important role in propionyl-CoA metabolism . Acetate kinase can also catalyze acetylation of CheY, increasing signal strength for flagellar rotation . A second gene encoding acetate kinase, G14, was thought to exist . Transcription of ackA is induced by the CreBC two-component system by minimal media growth conditions . Several metabolic genes, including ackA, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . E. coli double mutants deficient in AckA and Pta activity, or AckA and TdcD activity, were unable to metabolize threonine to propionate. This suggested the participation of this enzyme in pathway PWY-5437...

## Biological Role

Repressed by sdhX (gene.b4764). Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6A3|protein.P0A6A3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ackA; function=+
- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=ackA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007579,ECOCYC:EG10027,GeneID:946775`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2413470-2414672:+; feature_type=gene
