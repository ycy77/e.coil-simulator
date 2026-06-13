---
entity_id: "gene.b3094"
entity_type: "gene"
name: "exuR"
source_database: "NCBI RefSeq"
source_id: "gene-b3094"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3094"
  - "exuR"
---

# exuR

`gene.b3094`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3094`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

exuR (gene.b3094) is a gene entity. It encodes exuR (protein.P0ACL2). Encoded protein function: FUNCTION: Repressor for the exu regulon that encode genes involved in hexuronate utilization. It regulates the ExuT, UxaCA and UxuRAB operons. Binds D-tagaturonate and D-fructuronate as inducers. EcoCyc product frame: PD03270. Genomic coordinates: 3246652-3247428. EcoCyc protein note: The "Exuronate" repressor ExuR, is a DNA-binding transcription factor that negatively regulates its own synthesis and represses transcription of the operons involved in transport and catabolism of galacturonate and glucuronate . ExuR is similar to UxuR (49% of identity), and apparently both act together and are capable of cross-talk to regulate expression of the uxu operon . For this reason, there is the possibility that these regulators bind the same sites with different affinities. ExuR binds to the exuR regulatory region in the presence of glucuronate and inhibits the expression of exuR. This repression is partially affected by the presence of UxuR, since UxuR is capable of binding to the same regulatory region as ExuR . ExuR has been shown to act as a repressor that binds to a putative inverted repeat sequence . The promoter activity of exuR was increased during cell growth in the presence of glucuronate compared to growth with glucose as a main carbon source...

## Biological Role

Repressed by exuR (protein.P0ACL2), uxuR (protein.P39161). Activated by rpoD (protein.P00579), zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACL2|protein.P0ACL2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=exuR; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=exuR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL2|protein.P0ACL2]] `RegulonDB` `S` - regulator=ExuR; target=exuR; function=-
- `represses` <-- [[protein.P39161|protein.P39161]] `RegulonDB` `S` - regulator=UxuR; target=exuR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010176,ECOCYC:EG12739,GeneID:947602`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3246652-3247428:+; feature_type=gene
