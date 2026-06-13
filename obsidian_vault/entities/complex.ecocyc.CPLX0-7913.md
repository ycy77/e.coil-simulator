---
entity_id: "complex.ecocyc.CPLX0-7913"
entity_type: "complex"
name: "tellurite methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7913"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tellurite methyltransferase

`complex.ecocyc.CPLX0-7913`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7913`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25397|protein.P25397]]

## Enriched Summary

TehB was shown to have tellurite methyltransferase activity . TehB was earlier shown to cause a SAM-dependent loss of TeO32- from an assay mixture; the reaction product was unknown, but does not consist of a volatile form of methylated tellurium . The TehB protein in conjunction with TehA confers resistance to tellurite when expressed on a multicopy plasmid . Sequence analysis of TehB showed the presence of conserved sequence motifs occurring in S-adenosylmethionine (SAM)-dependent non-nucleic acid methyltransferases, and site-directed mutagenesis of conserved residues cause loss of tellurite resistance . Cysteine residues in TehB have also been shown to be involved in tellurite resistance . Dynamic light-scattering experiments show a conformational change upon addition of SAM and TeO32-, indicating that TehB binds both SAM and tellurite. Measurement of the hydrodynamic radius indicates that the protein is a dimer in solution ; the dimer form appears to be stabilized upon tellurite exposure . Crystal structures of TehB in the presence of the cofactor analogs SAH (1.48 Å resolution) and sinefungin (1.9 Å resolution) have been solved . The active site Arg177 residue was predicted from the structures and confirmed by site-directed mutagenesis...

## Biological Role

Catalyzes RXN0-6576 (reaction.ecocyc.RXN0-6576).

## Annotation

TehB was shown to have tellurite methyltransferase activity . TehB was earlier shown to cause a SAM-dependent loss of TeO32- from an assay mixture; the reaction product was unknown, but does not consist of a volatile form of methylated tellurium . The TehB protein in conjunction with TehA confers resistance to tellurite when expressed on a multicopy plasmid . Sequence analysis of TehB showed the presence of conserved sequence motifs occurring in S-adenosylmethionine (SAM)-dependent non-nucleic acid methyltransferases, and site-directed mutagenesis of conserved residues cause loss of tellurite resistance . Cysteine residues in TehB have also been shown to be involved in tellurite resistance . Dynamic light-scattering experiments show a conformational change upon addition of SAM and TeO32-, indicating that TehB binds both SAM and tellurite. Measurement of the hydrodynamic radius indicates that the protein is a dimer in solution ; the dimer form appears to be stabilized upon tellurite exposure . Crystal structures of TehB in the presence of the cofactor analogs SAH (1.48 Å resolution) and sinefungin (1.9 Å resolution) have been solved . The active site Arg177 residue was predicted from the structures and confirmed by site-directed mutagenesis . Tellurite resistance conferred by tehAB is limited to growth in rich medium and is dependent on the presence of a functional electron transport chain and functional quinone pool in the cell .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6576|reaction.ecocyc.RXN0-6576]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P25397|protein.P25397]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7913`
- `QSPROTEOME:QS00049674`

## Notes

2*protein.P25397
