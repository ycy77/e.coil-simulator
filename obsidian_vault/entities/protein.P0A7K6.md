---
entity_id: "protein.P0A7K6"
entity_type: "protein"
name: "rplS"
source_database: "UniProt"
source_id: "P0A7K6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplS b2606 JW2587"
---

# rplS

`protein.P0A7K6`

## Static

- Type: `protein`
- Source: `UniProt:P0A7K6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is located at the 30S-50S ribosomal subunit interface and may play a role in the structure and function of the aminoacyl-tRNA binding site. {ECO:0000255|HAMAP-Rule:MF_00402}.; FUNCTION: In the 70S ribosome it has been modeled to make two contacts with the 16S rRNA of the 30S subunit forming part of bridges B6 and B8 (PubMed:12809609). In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA (PubMed:16272117). The protein conformation is quite different between the 50S and 70S structures, which may be necessary for translocation (PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}. The L19 protein is a component of the 50S subunit of the ribosome. Depending on the method used, L19 does or does not appear to be essential for viability. L19 can be crosslinked to 23S rRNA , mRNA , and ribosomal proteins S9 and L18 , L3 , L14 , L6 , and L25 . L19 has RNA chaperone-like activity in an in vitro trans splicing assay as well as protein chaperone activity . L19 is photoaffinity labeled by dyhydrorosaramyicin . L19 appears to be phosphorylated at residues Ser18 and Ser82 . The phenotypes of mutants lacking L19 vary; a slow growth phenotype and accumulation of ribosome precursor particles during exponential growth and unbalanced synthesis of RNA have been reported...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: This protein is located at the 30S-50S ribosomal subunit interface and may play a role in the structure and function of the aminoacyl-tRNA binding site. {ECO:0000255|HAMAP-Rule:MF_00402}.; FUNCTION: In the 70S ribosome it has been modeled to make two contacts with the 16S rRNA of the 30S subunit forming part of bridges B6 and B8 (PubMed:12809609). In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA (PubMed:16272117). The protein conformation is quite different between the 50S and 70S structures, which may be necessary for translocation (PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2606|gene.b2606]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7K6`
- `KEGG:ecj:JW2587;eco:b2606;ecoc:C3026_14430;`
- `GeneID:86860728;93774456;947096;`
- `GO:GO:0000027; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0022625; GO:0070180`

## Notes

Large ribosomal subunit protein bL19 (50S ribosomal protein L19)
