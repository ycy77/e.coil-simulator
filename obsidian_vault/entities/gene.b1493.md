---
entity_id: "gene.b1493"
entity_type: "gene"
name: "gadB"
source_database: "NCBI RefSeq"
source_id: "gene-b1493"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1493"
  - "gadB"
---

# gadB

`gene.b1493`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1493`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadB (gene.b1493) is a gene entity. It encodes gadB (protein.P69910). Encoded protein function: FUNCTION: Converts glutamate to gamma-aminobutyrate (GABA), consuming one intracellular proton in the reaction. The gad system helps to maintain a near-neutral intracellular pH when cells are exposed to extremely acidic conditions. The ability to survive transit through the acidic conditions of the stomach is essential for successful colonization of the mammalian host by commensal and pathogenic bacteria. EcoCyc product frame: GLUTDECARBOXB-MONOMER. Genomic coordinates: 1570645-1572045. EcoCyc protein note: GadB, a glutamate decarboxylase enzyme, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions. There are two distinct E. coli GAD polypeptides which are highly similar to one another. AR2 also protects the cell during anaerobic phosphate starvation when glutamate is available by preventing damage from weak acids produced from carbohydrate fermentation. gadABC mutants have reduced viability after anaerobic phosphate starvation compared to wild-type . The crystal structure of GadB has been determined at acidic and neutral pH to resolutions of 2.0 and 2.3 Å, respectively . GadB is hexameric...

## Biological Role

Repressed by DNA-binding transcriptional regulator PtrR-L-glutamine (complex.ecocyc.CPLX0-10428), hns (protein.P0ACF8), lrp (protein.P0ACJ0), fliZ (protein.P52627), gadW (protein.P63201), csrA (protein.P69913). Activated by rpoD (protein.P00579), rpoS (protein.P13445), adiY (protein.P33234), gadX (protein.P37639), gadW (protein.P63201), gadE (protein.P63204), ydeO (protein.P76135), ydcI (protein.P77171), and 1 more.

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69910|protein.P69910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (15)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadB; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gadB; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=gadB; function=+
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadB; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=gadB; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P77171|protein.P77171]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=gadB; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadB; function=-+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=gadB; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0004976,ECOCYC:EG11490,GeneID:946058`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1570645-1572045:-; feature_type=gene
