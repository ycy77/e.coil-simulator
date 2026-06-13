---
entity_id: "gene.b2674"
entity_type: "gene"
name: "nrdI"
source_database: "NCBI RefSeq"
source_id: "gene-b2674"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2674"
  - "nrdI"
---

# nrdI

`gene.b2674`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2674`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdI (gene.b2674) is a gene entity. It encodes nrdI (protein.P0A772). Encoded protein function: FUNCTION: Probably involved in ribonucleotide reductase function. {ECO:0000250}. EcoCyc product frame: G7402-MONOMER. EcoCyc synonyms: ygaO. Genomic coordinates: 2800965-2801375. EcoCyc protein note: NrdI is a flavodoxin that mediates generation of the tyrosyl radical cofactor of NRDF-MONOMER NrdF, the β subunit of the class Ib ribonucleotide reductase. The nature of the metal ion cofactor for NrdF has been controversial, but results by indicate that the MnIII2-Y· form is the active form of NrdF and is generated from two HO2- anions supplied by NrdI. Crystal structures of MnII2-NrdF with reduced or oxidized NrdI show a channel connecting the flavin cofactor of NrdI to the NrdF active site . NrdI non-covalently binds FMN; the protein has unusual redox properties that allow it to catalyze the two-electron reduction of the Y· cluster of NrdF under anaerobic conditions, which serves to reactivate the ribonucleotide reductase enzyme . NrdI appears to specifically reduce NrdF, but not NrdB , and NrdI interacts directly with MnII2-NrdF . The nrdI gene is a conserved component of operons containing nrdE and nrdF . Expression of the nrdHIEF operon is increased by hydroxyurea and oxidative stress...

## Biological Role

Repressed by nrdR (protein.P0A8D0), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A772|protein.P0A772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdI; function=+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdI; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nrdI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008804,ECOCYC:G7402,GeneID:947158`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2800965-2801375:+; feature_type=gene
