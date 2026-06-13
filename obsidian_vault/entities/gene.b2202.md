---
entity_id: "gene.b2202"
entity_type: "gene"
name: "napC"
source_database: "NCBI RefSeq"
source_id: "gene-b2202"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2202"
  - "napC"
---

# napC

`gene.b2202`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2202`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napC (gene.b2202) is a gene entity. It encodes napC (protein.P0ABL5). Encoded protein function: FUNCTION: Mediates electron flow from quinones to the NapAB complex. EcoCyc product frame: NAPC-MONOMER. EcoCyc synonyms: yejX. Genomic coordinates: 2297657-2298259. EcoCyc protein note: The EG12060 gene encodes a membrane-bound tetraheme cytochrome c protein, which passes electrons either from menaquinone or from the CPLX0-3241 "NapGH ubiquinol-cytochrome c reductase complex" to the EG12061 NapB subunit of the NAP-CPLX "periplasmic nitrite reductase" . NapC is homologous to the G-55066 CymA protein of TAX-211586, which transfers electrons from menaquinol to a number of terminal oxidases. Heterologous expression of CymA in E. coli enabled growth with Fe(III) NTA as the terminal electron acceptor .

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABL5|protein.P0ABL5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napC; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napC; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napC; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napC; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napC; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napC; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napC; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=napC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007281,ECOCYC:EG12060,GeneID:946706`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2297657-2298259:-; feature_type=gene
