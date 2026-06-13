---
entity_id: "gene.b2195"
entity_type: "gene"
name: "ccmG"
source_database: "NCBI RefSeq"
source_id: "gene-b2195"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2195"
  - "ccmG"
---

# ccmG

`gene.b2195`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2195`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmG (gene.b2195) is a gene entity. It encodes dsbE (protein.P0AA86). Encoded protein function: FUNCTION: Involved in disulfide bond formation. Catalyzes a late, reductive step in the assembly of periplasmic c-type cytochromes, probably the reduction of disulfide bonds of the apocytochrome c to allow covalent linkage with the heme. Possible subunit of a heme lyase. DsbE is maintained in a reduced state by DsbD. EcoCyc product frame: EG12053-MONOMER. EcoCyc synonyms: yejQ, dsbE. Genomic coordinates: 2292407-2292964. EcoCyc protein note: CcmG is a membrane-anchored thiol-disulfide reductase implicated in apocytochrome c thioreduction prior to heme ligation in the System I pathway of cytochome c maturation. ccmG is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmG deletion mutant is able to produce (plasmid-encoded) apocytochrome c-550 but not holocytochrome c-550 . CcmG is a small protein with a thioredoxin-like motif facing the periplasm, but tethered to the cytoplasmic membrane by a hydrophobic N-terminal domain; CcmG has a reducing role in vivo...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA86|protein.P0AA86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmG; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmG; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmG; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmG; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmG; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007264,ECOCYC:EG12053,GeneID:949073`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2292407-2292964:-; feature_type=gene
