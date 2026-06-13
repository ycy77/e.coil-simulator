---
entity_id: "gene.b0237"
entity_type: "gene"
name: "pepD"
source_database: "NCBI RefSeq"
source_id: "gene-b0237"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0237"
  - "pepD"
---

# pepD

`gene.b0237`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0237`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepD (gene.b0237) is a gene entity. It encodes pepD (protein.P15288). Encoded protein function: FUNCTION: Dipeptidase with broad substrate specificity. Requires dipeptide substrates with an unblocked N-terminus and the amino group in the alpha or beta position. Non-protein amino acids and proline are not accepted in the C-terminal position, whereas some dipeptide amides and formyl amino acids are hydrolyzed. Also shows cysteinylglycinase activity, which is sufficient for E.coli to utilize cysteinylglycine as a cysteine source. {ECO:0000269|PubMed:11157967, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:355237, ECO:0000269|PubMed:7988883}. EcoCyc product frame: EG10695-MONOMER. EcoCyc synonyms: pepH. Genomic coordinates: 254259-255716. EcoCyc protein note: Peptidase D (PepD) is a dipeptidase capable of breaking down a number of dipeptides with unblocked N termini , including cysteinylglycine, a breakdown product of glutathione . Neither proline nor non-protein amino acids are accepted in the C-terminal position . Transcription of pepD increases five fold during phosphate starvation . Overexpression of pepD negatively affects biofilm formation . Using a method that distinguishes N-phosphorylation from O-phosphorylation, N-phosphorylation was detected in vitro .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15288|protein.P15288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pepD; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=pepD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000809,ECOCYC:EG10695,GeneID:945013`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:254259-255716:-; feature_type=gene
