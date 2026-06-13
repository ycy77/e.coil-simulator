---
entity_id: "protein.P0ABK5"
entity_type: "protein"
name: "cysK"
source_database: "UniProt"
source_id: "P0ABK5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysK cysZ b2414 JW2407"
---

# cysK

`protein.P0ABK5`

## Static

- Type: `protein`
- Source: `UniProt:P0ABK5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: (Microbial infection) In addition to its role in cysteine synthesis, stimulates the tRNase activity of CdiA-CT from E.coli strain 536 / UPEC; stimulation does not require O-acetylserine sulfhydrylase activity. CdiA is the toxic component of a toxin-immunity protein module, which functions as a cellular contact-dependent growth inhibition (CDI) system. CDI modules allow bacteria to communicate with and inhibit the growth of closely related neighboring bacteria in a contact-dependent fashion (experiments done in strains BW25113 and X90, both K12 derivatives). This protein is not required for CDI of strain EC93, whose toxin may function by forming inner cell membrane pores (PubMed:22333533). CysK stabilizes CdiA-CT, allowing it to bind tRNA substrate; neither CdiA-CT nor CysK bind tRNA alone in vitro (PubMed:27531961). {ECO:0000269|PubMed:22333533, ECO:0000269|PubMed:27531961}.

## Biological Role

Catalyzes O-phospho-L-serine:hydrogen-sulfide 2-amino-2-carboxyethyltransferase (reaction.R07274). Component of cysteine synthase A (complex.ecocyc.ACSERLYA-CPLX), cysteine synthase complex (complex.ecocyc.CYSSYNMULTI-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: (Microbial infection) In addition to its role in cysteine synthesis, stimulates the tRNase activity of CdiA-CT from E.coli strain 536 / UPEC; stimulation does not require O-acetylserine sulfhydrylase activity. CdiA is the toxic component of a toxin-immunity protein module, which functions as a cellular contact-dependent growth inhibition (CDI) system. CDI modules allow bacteria to communicate with and inhibit the growth of closely related neighboring bacteria in a contact-dependent fashion (experiments done in strains BW25113 and X90, both K12 derivatives). This protein is not required for CDI of strain EC93, whose toxin may function by forming inner cell membrane pores (PubMed:22333533). CysK stabilizes CdiA-CT, allowing it to bind tRNA substrate; neither CdiA-CT nor CysK bind tRNA alone in vitro (PubMed:27531961). {ECO:0000269|PubMed:22333533, ECO:0000269|PubMed:27531961}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R07274|reaction.R07274]] `KEGG` `database` - via EC:2.5.1.47
- `is_component_of` --> [[complex.ecocyc.ACSERLYA-CPLX|complex.ecocyc.ACSERLYA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CYSSYNMULTI-CPLX|complex.ecocyc.CYSSYNMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2414|gene.b2414]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABK5`
- `KEGG:ecj:JW2407;eco:b2414;ecoc:C3026_13420;`
- `GeneID:86860557;93774717;946877;`
- `GO:GO:0004124; GO:0005737; GO:0005829; GO:0006535; GO:0008652; GO:0009333; GO:0016740; GO:0030170; GO:0042802; GO:0042803; GO:0050272; GO:0080146`
- `EC:2.5.1.47; 4.5.1.5`

## Notes

Cysteine synthase A (CSase A) (EC 2.5.1.47) (O-acetylserine (thiol)-lyase A) (OAS-TL A) (O-acetylserine sulfhydrylase A) (S-carboxymethylcysteine synthase) (EC 4.5.1.5) (Sulfate starvation-induced protein 5) (SSI5)
