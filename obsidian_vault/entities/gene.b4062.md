---
entity_id: "gene.b4062"
entity_type: "gene"
name: "soxS"
source_database: "NCBI RefSeq"
source_id: "gene-b4062"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4062"
  - "soxS"
---

# soxS

`gene.b4062`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4062`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

soxS (gene.b4062) is a gene entity. It encodes soxS (protein.P0A9E2). Encoded protein function: FUNCTION: Transcriptional activator of the superoxide response regulon of E.coli that includes at least 10 genes such as sodA, nfo, zwf and micF. Binds the DNA sequence 5'-GCACN(7)CAA-3'. It also facilitates the subsequent binding of RNA polymerase to the micF and the nfo promoters. EcoCyc product frame: PD00406. Genomic coordinates: 4277060-4277383. EcoCyc protein note: SoxS is a dual transcriptional activator and participates in the removal of superoxide and nitric oxide and protection from organic solvents and antibiotics . SoxS shares 49% identity with MarA and the N-terminal domain of Rob . These proteins activate a common set of about 50 target genes , the marA/soxS/rob regulon, involved in antibiotic resistance , superoxide resistance , and tolerance to organic solvents and heavy metals . The activity of each protein is induced by different signals: the activity of Rob is increased with dipyridyl, bile salts, or decanoate , and the activities of MarA and SoxS are increased by the aromatic weak acid salicylate and by oxidative stress , respectively. SoxS was induced by tellurite (TeO32-) in a DNA microarray analysis . Many genes are regulated by all three proteins; however, some genes are regulated by only one of them...

## Biological Role

Repressed by mgrR (gene.b4698), soxS (protein.P0A9E2), acrR (protein.P0ACS9). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), soxR (protein.P0ACS2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9E2|protein.P0A9E2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=soxS; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `C` - regulator=SoxR; target=soxS; function=+
- `represses` <-- [[gene.b4698|gene.b4698]] `RegulonDB` `S` - regulator=MgrR; target=soxS; function=-
- `represses` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=soxS; function=-
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `S` - regulator=AcrR; target=soxS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013311,ECOCYC:EG10958,GeneID:948567`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4277060-4277383:-; feature_type=gene
