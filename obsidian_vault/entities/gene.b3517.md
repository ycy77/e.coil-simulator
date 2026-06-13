---
entity_id: "gene.b3517"
entity_type: "gene"
name: "gadA"
source_database: "NCBI RefSeq"
source_id: "gene-b3517"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3517"
  - "gadA"
---

# gadA

`gene.b3517`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3517`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadA (gene.b3517) is a gene entity. It encodes gadA (protein.P69908). Encoded protein function: FUNCTION: Converts glutamate to gamma-aminobutyrate (GABA), consuming one intracellular proton in the reaction. The gad system helps to maintain a near-neutral intracellular pH when cells are exposed to extremely acidic conditions. The ability to survive transit through the acidic conditions of the stomach is essential for successful colonization of the mammalian host by commensal and pathogenic bacteria. EcoCyc product frame: GLUTDECARBOXA-MONOMER. EcoCyc synonyms: gadS. Genomic coordinates: 3666180-3667580. EcoCyc protein note: GadA, a glutamate decarboxylase enzyme, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions. There are two distinct E. coli GAD polypeptides which are highly similar to one another. AR2 also protects the cell during anaerobic phosphate starvation when glutamate is available by preventing damage from weak acids produced from carbohydrate fermentation. gadABC mutants have reduced viability after anaerobic phosphate starvation compared to wild-type . The crystal structure of the hexameric GadA in complex with the substrate analog glutarate has been determined to a resolution of 2.05 Å . Regulation has been described...

## Biological Role

Repressed by DNA-binding transcriptional regulator PtrR-L-glutamine (complex.ecocyc.CPLX0-10428), hns (protein.P0ACF8), rcsB (protein.P0DMC7), gadW (protein.P63201), csrA (protein.P69913). Activated by rpoD (protein.P00579), rpoS (protein.P13445), adiY (protein.P33234), gadX (protein.P37639), gadW (protein.P63201), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

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

- `encodes` --> [[protein.P69908|protein.P69908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (11)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadA; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gadA; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=gadA; function=+
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadA; function=-+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gadA; function=-
- `represses` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=gadA; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadA; function=-+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=gadA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0011490,ECOCYC:EG50009,GeneID:948027`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3666180-3667580:-; feature_type=gene
