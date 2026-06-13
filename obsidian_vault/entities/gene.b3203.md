---
entity_id: "gene.b3203"
entity_type: "gene"
name: "hpf"
source_database: "NCBI RefSeq"
source_id: "gene-b3203"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3203"
  - "hpf"
---

# hpf

`gene.b3203`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3203`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hpf (gene.b3203) is a gene entity. It encodes hpf (protein.P0AFX0). Encoded protein function: FUNCTION: During stationary phase, promotes and stabilizes dimerization of 70S ribosomes by the ribosome modulation factor (RMF), leading to the formation of inactive 100S ribosomes (PubMed:18174192). Converts immature 90S particles formed by RMF into 100S ribosomes (PubMed:16324148). Crystallization with T.thermophilus 70S ribosomes shows it binds in the channel between the head and body of the 30S subunit, where mRNA, tRNAs, initiation factors IF1 and IF3 and elongation factor G would bind; however RMF is still able to bind (PubMed:22605777). In this crystal binding of HPF induces movement of the 30S head domain away from the rest of the ribosome, presumably so they would more easily form dimers (PubMed:22605777). May also function as a potential translational inhibitor (PubMed:18174192). {ECO:0000269|PubMed:11168583, ECO:0000269|PubMed:16324148, ECO:0000269|PubMed:18174192, ECO:0000269|PubMed:19170772, ECO:0000269|PubMed:22605777}. EcoCyc product frame: EG11681-MONOMER. EcoCyc synonyms: yhbH. Genomic coordinates: 3346173-3346460. EcoCyc protein note: The hibernation factors HPF, EG50004-MONOMER RMF and EG11151-MONOMER RaiA protect ribosomes, likely by protecting ribonuclease target sites within the ribosome . HPF binds to 100S ribosome dimers at stationary phase...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by hfq (protein.P0A6X3), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFX0|protein.P0AFX0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A6X3|protein.P0A6X3]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=hpf; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010516,ECOCYC:EG11681,GeneID:947718`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3346173-3346460:+; feature_type=gene
