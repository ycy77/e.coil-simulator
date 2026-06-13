---
entity_id: "gene.b0894"
entity_type: "gene"
name: "dmsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0894"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0894"
  - "dmsA"
---

# dmsA

`gene.b0894`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0894`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmsA (gene.b0894) is a gene entity. It encodes dmsA (protein.P18775). Encoded protein function: FUNCTION: Catalyzes the reduction of dimethyl sulfoxide (DMSO) to dimethyl sulfide (DMS). DMSO reductase serves as the terminal reductase under anaerobic conditions, with DMSO being the terminal electron acceptor. Terminal reductase during anaerobic growth on various sulfoxides and N-oxide compounds. Allows E.coli to grow anaerobically on DMSO as respiratory oxidant. {ECO:0000269|PubMed:3062312}. EcoCyc product frame: DMSA-MONOMER. Genomic coordinates: 940959-943403. EcoCyc protein note: The DmsA subunit of DMSO reductase contains a molybdo-bis(pyranopterin guanine dinucleotide) (Mo-bisPGD) cofactor and a [4Fe-4S] cluster (known as FS0) . DmsA contains a twin-arginine leader peptide which targets the protein to the membrane, although DmsA does not appear to be exported to the periplasm. The leader peptide is also essential for expression of DmsA and stability of the DmsAB dimer, and is cleaved between residues 45 and 46 . The leader peptide interacts with the redox enzyme maturation protein (REMP) G6849-MONOMER "DmsD" .

## Biological Role

Repressed by modE (protein.P0A9G8), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18775|protein.P18775]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dmsA; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dmsA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=dmsA; function=+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=dmsA; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dmsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003044,ECOCYC:EG10232,GeneID:945508`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:940959-943403:+; feature_type=gene
