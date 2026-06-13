---
entity_id: "gene.b1987"
entity_type: "gene"
name: "cbl"
source_database: "NCBI RefSeq"
source_id: "gene-b1987"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1987"
  - "cbl"
---

# cbl

`gene.b1987`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1987`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbl (gene.b1987) is a gene entity. It encodes cbl (protein.Q47083). Encoded protein function: FUNCTION: May be an accessory regulatory protein within the cys regulon. EcoCyc product frame: G7071-MONOMER. Genomic coordinates: 2059964-2060914. EcoCyc protein note: The transcription factor Cbl, for "cysB like," is a regulator involved in the expression of genes required for aliphatic sulfonate utilization and homeostatic response to sulfate starvation . Cbl does not require a ligand to bind to its DNA-binding site, but the activity of this protein is negatively regulated by the adenosine 5'-phophosulfate (APS) cofactor . This protein belongs to the large LysR family of transcriptional regulators and it is positively regulated by CysB, which is similar to Cbl (40% identity) . Members of this family have two domains, an N-terminal domain with a helix-turn-helix DNA-binding motif and a large C-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like Cbl, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The crystal structure of the C-terminal regulatory domain of Cbl (2.8Å) has been solved...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by NtrC phosphorylated dimer (complex.ecocyc.CPLX0-8566), cysB (protein.P0A9F3), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47083|protein.Q47083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cbl; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006590,ECOCYC:G7071,GeneID:946502`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2059964-2060914:-; feature_type=gene
