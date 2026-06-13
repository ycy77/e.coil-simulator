---
entity_id: "gene.b1262"
entity_type: "gene"
name: "trpC"
source_database: "NCBI RefSeq"
source_id: "gene-b1262"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1262"
  - "trpC"
---

# trpC

`gene.b1262`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1262`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpC (gene.b1262) is a gene entity. It encodes trpC (protein.P00909). Encoded protein function: FUNCTION: Bifunctional enzyme that catalyzes two sequential steps of tryptophan biosynthetic pathway. The first reaction is catalyzed by the isomerase, coded by the TrpF domain; the second reaction is catalyzed by the synthase, coded by the TrpC domain. EcoCyc product frame: PRAI-IGPS. EcoCyc synonyms: trpF, trpCF. Genomic coordinates: 1318427-1319788. EcoCyc protein note: Bifunctional phosphoribosylanthranilate isomerase / indole-3-glycerol phosphate synthase (TrpC) carries out the third and fourth steps in the tryptophan biosynthesis pathway. The phosphoribosylanthranilate isomerase activity of TrpC catalyzes the Amadori rearrangement of its substrate into carboxyphenylaminodeoxyribulose phosphate . The indole-glycerol phosphate synthase activity of TrpC catalyzes the ring closure of this product to yield indole-3-glycerol phosphate . Early mutant studies identified N-(5'-phosphoribosyl)-anthranilate (PRA) and 1-(o-carboxyphenylamino)-1'-deoxyribulose-5'-phosphate (CDRP) as intermediates in the biosynthesis of tryptophan and provided evidence that a single polypeptide chain catalyzes both the conversion of PRA to CDRP and CDRP to indole-3-glycerol-phosphate (IGP)...

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00909|protein.P00909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpC; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpC; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004238,ECOCYC:EG11026,GeneID:945519`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1318427-1319788:-; feature_type=gene
